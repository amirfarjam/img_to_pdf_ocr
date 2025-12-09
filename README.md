# Image to PDF OCR Pipeline

This repository provides a complete image-to-PDF processing pipeline for
converting screenshots, scanned notes, and long images into A4-formatted
PDFs, with optional OCR support.

It is designed for: - Long screenshots and scrolling captures - Lecture
slides and course material - Research documentation - Custom GPT
knowledge ingestion - Archival-quality searchable PDFs

This project supports two main workflows:

1.  Image-only PDF generation for professional OCR using Adobe Acrobat
    Pro DC
2.  Fully automatic OCR processing using Python and Tesseract

## Project Structure

    .
    ├── .git/
    ├── .gitignore
    ├── .vscode/
    ├── image_to_pdf.py
    ├── img_to_pdf_ocr.py
    ├── input_images/
    ├── output_pdf_image/
    └── output_pdf_ocr/

## Folder Descriptions

### input_images/

This folder contains all source images such as: - Long screenshots -
Slide captures - Scanned notes

These files are ignored by Git.

### output_pdf_image/

This folder stores: - Image-only PDF files generated for Adobe Acrobat
Pro DC OCR

These files are auto-generated and ignored by Git.

### output_pdf_ocr/

This folder stores: - Final searchable OCR-enabled PDF files

These files are auto-generated and ignored by Git.

## Python Scripts

### image_to_pdf.py

Purpose:\
Converts images into a pure image-only multi-page A4 PDF without
performing OCR.

Key features: - Splits very long images into multiple A4-sized pages -
Preserves full image quality - Sorts images by creation date - Produces
clean input for Adobe Acrobat Pro DC OCR

Typical workflow: input_images -\> image_to_pdf.py -\> output_pdf_image
-\> Adobe Acrobat OCR

### img_to_pdf_ocr.py

Purpose:\
Provides a fully automatic OCR PDF generation pipeline using Python.

Key features: - Splits long images into A4 pages - Runs OCR
automatically using Tesseract - Embeds searchable and selectable text -
Outputs final PDFs into output_pdf_ocr

Typical workflow: input_images -\> img_to_pdf_ocr.py -\> output_pdf_ocr

Note:\
This version provides searchable text but does not achieve pixel-perfect
text alignment compared to Adobe Acrobat OCR.

## Recommended Professional Workflow

For highest OCR accuracy and perfect text alignment:

1.  Place images into input_images
2.  Run image_to_pdf.py
3.  Open the resulting PDF in Adobe Acrobat Pro DC
4.  Use Tools -\> Scan & OCR -\> Recognize Text
5.  Save the final searchable PDF

This produces professional-quality searchable PDFs suitable for research
archiving and Custom GPT ingestion.

## How to Run

Image-only PDF generation:

    python image_to_pdf.py

Automatic OCR PDF generation:

    python img_to_pdf_ocr.py

## Dependencies

Install required packages:

    pip install pillow reportlab pytesseract

Install the OCR engine on macOS:

    brew install tesseract

## Use Cases

-   Course slide archiving
-   Lecture recording screenshots
-   Research documentation
-   Knowledge base creation for Custom GPT
-   Scanned handwritten notes

## Notes

If Adobe Acrobat Pro DC is available, it is recommended to use
image_to_pdf.py followed by Acrobat's Scan and OCR tool for best-quality
OCR results.
