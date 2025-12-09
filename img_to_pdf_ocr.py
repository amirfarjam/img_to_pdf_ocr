import os
import math
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import Color

# =========================
# CONFIGURATION
# =========================

IMAGE_FOLDER = "input_images"
OUTPUT_PDF = "output_pdf/course_material_ocr.pdf"

os.makedirs("output_pdf", exist_ok=True)

# =========================
# PDF SETUP
# =========================

pdf_width, pdf_height = A4  # in points (~595 x 842)
c = canvas.Canvas(OUTPUT_PDF, pagesize=A4)

# =========================
# CREATION-TIME SORTING
# =========================

def get_creation_time(path):
    stat = os.stat(path)

    # macOS: true creation time
    if hasattr(stat, "st_birthtime"):
        return stat.st_birthtime

    # Windows/Linux fallback
    return stat.st_ctime


files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"))
]

files_sorted_by_time = sorted(
    files,
    key=lambda f: get_creation_time(os.path.join(IMAGE_FOLDER, f))
)

# =========================
# IMAGE PROCESSING FUNC
# =========================

def process_image(image_path: str):
    img = Image.open(image_path).convert("RGB")
    img_w, img_h = img.size

    # A4 aspect ratio in PDF space
    aspect_ratio = pdf_height / pdf_width  # ~1.414

    # Compute slice height in IMAGE pixels
    slice_height_px = int(img_w * aspect_ratio)

    if slice_height_px <= 0:
        slice_height_px = img_h

    num_slices = math.ceil(img_h / slice_height_px)

    print(f"  → Slicing into {num_slices} page(s)")

    for i in range(num_slices):
        top = i * slice_height_px
        bottom = min((i + 1) * slice_height_px, img_h)

        # ---- Crop vertical slice ----
        slice_img = img.crop((0, top, img_w, bottom))

        # ---- OCR this slice ----
        text = pytesseract.image_to_string(slice_img)

        # ---- Draw image FULL PAGE ----
        image_reader = ImageReader(slice_img)

        c.drawImage(
            image_reader,
            0,
            0,
            width=pdf_width,
            height=pdf_height,
            preserveAspectRatio=True,
            anchor='sw'
        )

        # ---- Add lightly invisible OCR text layer ----
        text_obj = c.beginText()
        text_obj.setTextOrigin(0.5 * inch, pdf_height - 0.5 * inch)
        text_obj.setFont("Helvetica", 8)

        # Almost invisible but searchable
        text_obj.setFillColor(Color(0, 0, 0, alpha=0.01))

        for line in text.splitlines():
            text_obj.textLine(line)

        c.drawText(text_obj)
        c.showPage()

# =========================
# MAIN LOOP (TIME SORTED)
# =========================

for filename in files_sorted_by_time:
    image_path = os.path.join(IMAGE_FOLDER, filename)
    print(f"Processing: {filename}")
    process_image(image_path)

# =========================
# SAVE PDF
# =========================

c.save()
print("\n Done! Searchable PDF created at:")
print("➡", OUTPUT_PDF)
