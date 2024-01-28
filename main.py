# Import the necessary libraries
from PIL import Image  # PIL (Pillow) is a library to open, manipulate, and save many different image file formats
import pytesseract  # pytesseract is an OCR tool for python (a wrapper for Google’s Tesseract-OCR Engine)

# Define a list of image paths. In this case, we have two images: 'img1.png' and 'img2.png'.
# These images are presumably located in the same directory as this script.
# If they're located in a different directory, you should provide the full path to the images.
image_paths = ['img1.png', 'img2.png']

# Initialize an empty list to store the extracted text from each image
extracted_texts = []

# Loop over each image path in the image_paths list
for path in image_paths:
    # Open the image file
    img = Image.open(path)
    
    # Use pytesseract to extract text from the image
    # The 'lang' parameter is set to 'fra' to indicate that the text in the image is in French
    text = pytesseract.image_to_string(img, lang='fra')
    
    # Append the extracted text to the extracted_texts list
    extracted_texts.append(text)

# Print the list of extracted texts
# Each element in the list corresponds to the text extracted from one image
if '__main__' == __name__:
    print(extracted_texts)
