import sys
import os
import re
import cv2

class MemeOCR:
    def __init__(self):
        self._white_thresh = 240
        self._tmp_image_fname = '/tmp/memeocr.jpg'
        self._tmp_txt_base = '/tmp/memeocr'
        self._tmp_txt_fname = self._tmp_txt_base + '.txt'

    def _thresh_words(self, fname):
        try:
            img = cv2.imread(fname)
        except IOError:
            return False
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if all([elem >= self._white_thresh for elem in img[i][j]]):
                    img[i][j] = (255, 255, 255)
                else:
                    img[i][j] = (0, 0, 0)

        cv2.imwrite(self._tmp_image_fname, img)
        return True

    def _exec_tesseract(self):
        cmd = 'env TESSDATA_PREFIX=./ tesseract -l joh %s %s > /dev/null' % (self._tmp_image_fname, self._tmp_txt_base)
        ret = os.system(cmd)
        return ret == 0

    def _read_txt(self):
        try:
            fr = open(self._tmp_txt_fname)
        except IOError:
            return None
        content = fr.read()
        fr.close()
        blocks = re.split(r'\n\n', content)
        lines = [re.sub(r'\s+', ' ', block) for block in blocks if block.strip()]
        return lines

    def _delete_tmp_files(self):
        if os.path.exists(self._tmp_image_fname):
            os.remove(self._tmp_image_fname)
        if os.path.exists(self._tmp_txt_fname):
            os.remove(self._tmp_txt_fname)

    def recognize(self, fname):
        if not self._thresh_words(fname):
            self._delete_tmp_files()
            return None
        if not self._exec_tesseract():
            self._delete_tmp_files()
            return None
        txt = self._read_txt()
        self._delete_tmp_files()
        return txt

