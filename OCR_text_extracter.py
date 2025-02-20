import os
from PIL import Image
import pytesseract

# Path to the folder containing images
folder_path = r"C:\Users\jyoji\Downloads\6.Dominant Firm Unilateral Conduct Monopolization and Abuse of Dominance (1)"

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# List to store extracted text from each image
extracted_text = []

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check if the file is an image (you can add more formats if needed)
        image_path = os.path.join(folder_path, filename)  # Get full path of the image
        try:
            # Load the image
            image = Image.open(image_path)
            
            # Perform OCR on the image
            text = pytesseract.image_to_string(image)
            
            # Append the text to the list
            extracted_text.append(text)
            
            print(f"Extracted text from {filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Combine all extracted text into a single string
all_text = "\n".join(extracted_text)

# Save the extracted text to a file
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)

print("Text extraction complete and saved to 'extracted_text_mult.txt'")
