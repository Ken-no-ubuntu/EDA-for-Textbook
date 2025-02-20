import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ensure this path is correct

# Test Tesseract by running it directly
try:
    text = pytesseract.image_to_string('path/to/a/test/image.jpg')  # Replace with a test JPG image
    print(text)
except Exception as e:
    print(e)
