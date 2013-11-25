import sys
import numpy
import cv2

def main(argv):
    thresh1 = 210

    ori = cv2.imread('ori.jpg')
    shape = ori.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if all([elem >= thresh1 for elem in ori[i][j]]):
                ori[i][j] = (255, 255, 255)
            else:
                ori[i][j] = (0, 0, 0)

    cv2.imwrite('bin.jpg', ori)

if __name__ == '__main__':
    main(sys.argv)

