# Meme OCR

This is an optical character recognition (OCR) tool using [Tesseract][1] specifically for internet meme images.


## Requirement

- Install the `tesseract` executable by [this tutorial][2]
- Install Python OpenCV package by:

```
$ sudo pip3 install opencv-python
```


## Usage

1. Prepare your meme image (e.g. `/path/to/your/some-crazy-meme.jpg`).
2. Just run:

```
$ ./main.py /path/to/your/some-crazy-meme.jpg
```

And the recognized texts will be printed in the stdout.


## Examples

```
$ ./main.py ./examples/socially-awkward-penguin.jpg
```


[1]: https://github.com/tesseract-ocr/tesseract
[2]: https://tesseract-ocr.github.io/tessdoc/Home.html
