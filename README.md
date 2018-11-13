# Meme OCR

This is an optical character recognition (OCR) tool using [Tesseract][1] specifically for internet meme images.

A dedicated trained Tesseract model is included.


## Requirement

- Install the `tesseract` executable by [this tutorial](https://github.com/tesseract-ocr/tesseract/wiki).
- Install Python OpenCV package by:

```
$ sudo pip install opencv-python
```


## Usage

1. Prepare your meme image (e.g. `/path/to/your/some-crazy-meme.jpg`).
2. Just run:

```
$ ./main.py /path/to/your/some-crazy-meme.jpg
```

And the recognized texts will be printed in the stdout.


[1]: https://code.google.com/p/tesseract-ocr/
