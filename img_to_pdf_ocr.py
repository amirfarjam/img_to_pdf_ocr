import os
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


IMAGE_FOLDER = "input_images"
OUTPUT_PDF = "output_pdf/pdf_ocr.pdf"


# Create PDF
c = canvas.Canvas(OUTPUT_PDF, pagesize=A4)
width, height = A4

for filename in sorted(os.listdir(IMAGE_FOLDER)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp")):
        image_path = os.path.join(IMAGE_FOLDER, filename)
        print(f"OCR processing: {filename}")

        img = Image.open(image_path)

        # Run OCR
        text = pytesseract.image_to_string(img)

        # Add extracted text to PDF
        text_object = c.beginText()
        text_object.setTextOrigin(1 * inch, height - 1 * inch)
        text_object.setFont("Helvetica", 10)

        for line in text.split("\n"):
            text_object.textLine(line)

        c.drawText(text_object)
        c.showPage()

c.save()

print("\n Searchable PDF created:", OUTPUT_PDF)
