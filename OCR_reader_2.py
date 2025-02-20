
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the JPG image
image_path = image_path = r"C:\Users\jyoji\Downloads\6.Dominant Firm Unilateral Conduct Monopolization and Abuse of Dominance (1)\1729421317996-8b80b286-4bf4-4c0a-a775-d6ccc61b1d8dDominant Firm Unilateral Conduct Monopolization and Abuse of Dominance (1)_1.jpg"  # Replace with your actual image path
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print or save the extracted text
print(text)

# Optionally, save the extracted text to a file
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
