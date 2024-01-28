from PIL import Image
import pytesseract

# Let's load the images uploaded by the user to extract the text
image_paths = ['img1.png', 
               'img2.png',]

# Extract text from images using pytesseract
extracted_texts = []
for path in image_paths:
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='fra')
    extracted_texts.append(text)

print(extracted_texts)
