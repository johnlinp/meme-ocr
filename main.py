from memeocr import MemeOCR

ocr = MemeOCR()
txt = ocr.recognize('input-memes/6947689.jpg')
print txt[0]
print txt[1]
