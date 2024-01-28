# Text Extraction from Images using Tesseract OCR

This Python script uses the Tesseract OCR (Optical Character Recognition) engine to extract text from images. The script is currently set up to extract French text from two images: 'img1.png' and 'img2.png'.

## Dependencies

The script depends on the following Python libraries:

- Pillow (PIL): A library to open, manipulate, and save many different image file formats.
- pytesseract: An OCR tool for Python (a wrapper for Google’s Tesseract-OCR Engine).

You can install these dependencies using pip:

```sh
pip install Pillow pytesseract
```

## Usage

To use the script, simply run it with Python:

```sh
python test.py
```

The script will print out a list of extracted texts. Each element in the list corresponds to the text extracted from one image.

## Customization

You can customize the script to suit your needs:

- To extract text from different images, modify the `image_paths` list with the paths to your images.
- To extract text in a different language, change the `lang` parameter in the `pytesseract.image_to_string` function to the appropriate language code.

---

Please note that Tesseract supports many languages, but you need to install the corresponding language data file for each language. You can find more information about this in the [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Data-Files.html).
