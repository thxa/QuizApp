import fitz  # PyMuPDF
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Step 1: Extract images from the PDF
def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(f"page_{i + 1}.png")
                images.append(f"page_{i + 1}.png")
            else:               # CMYK: convert to RGB first
                pix = fitz.Pixmap(fitz.csRGB, pix)
                pix.writePNG(f"page_{i + 1}.png")
                images.append(f"page_{i + 1}.png")
            pix = None
    return images

# Step 2: Read text from the JSON file
def read_text_from_json(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

# Step 3: Combine images and text into a new PDF
def create_new_pdf(images, texts, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    for i, image_path in enumerate(images):
        c.drawImage(image_path, 0, 0, width=width, height=height)
        c.setFont("Helvetica", 12)
        text = texts.get(str(i + 1), "")  # Get text for the page, default to empty if not found
        text_object = c.beginText(40, height - 40)
        text_object.textLines(text)
        c.drawText(text_object)
        c.showPage()
    c.save()

# Usage example
pdf_path = "your_pdf_file.pdf"
json_path = "your_text_file.json"
output_path = "output.pdf"

images = extract_images_from_pdf(pdf_path)
texts = read_text_from_json(json_path)
create_new_pdf(images, texts, output_path)

