import requests 
import json



#|%%--%%| <9ypDFLV63a|oL5jMOz3aa>

ck = "drive"
ds = "APznzaYz1eQxaF1u0g3Mj0RsGeL8LmZEzL-1A2_N1X5ATSZ_prbKpz6dmJV6nYVgfUBGLnMiHuPoT6vspGlYdeROU60kfgt-eLp4zePdCeFuCie_dHcxl3G6SlQlebovAorTka2_HV3yLNynjRF31HGv9Vtev0Cwx97q6A99Wdlc1DGWQev6TUZAgrfhtntDhxDmnhasg0h0eBGzxwGZI2lZVrYkJ7Rqiru1J2pUgcfi1m-_oroBrB-J_l2J67Qhh3jUHN8mgoc2N7zRhjD2VgkBQ0H6-AXzFcvVXEe5xSVxiJCsD-A3XcBmiv2wZWn1506noI3Lxov3UAEnVhibjCrYYbSKHM0axJ6H1eIdzUbUN5iR1y4JRyCTHAXp3yaQ7UKyY7KvkhVDf8h9Jq5eFlkGW8AeyC7aTw=="
authuser = 0 
page = 4




url_ = f"https://drive.google.com/viewer2/prod-03/presspage?ck={ck}&ds={ds}&authuser={authuser}&page={page}"

#|%%--%%| <oL5jMOz3aa|blQVch9jTm>


# https://drive.google.com/viewer2/prod-03/presspage?ck=drive&ds=APznzaZtuM1mjnWBkoHQuv0P6A5Zv4TMmrvgNeEwVYdSIPbg3_EYu8uTStHC8knRAmTA6RhrzPTjA89co5IHS7_MbFHBP1F7-l3dG5kaPASnurFYqiH7xklzWRhC2ad8sPteVg7VZ6qj-7zJIM74DhoHGZhrRI5xgWxekS_FIkvCAK14_1M3A08cgUwVbMh6uQDFx39z-mFF-KFV9Eoy2iJVt9R2tGfpyT3pZ1VQY2XA0eNmOcvJy-Npi1msOl4jBJqheLuj19OU0VCWDa0ur4U2Cu7q54n2EN6EPe9Rv0u08joZnMBNAWjxRM9QqbuBmTbkFQxzKyBMTHrGLkFfanLMRMCv-7wkuP1_JeIRV3We8shNEOsJkqpSwIYJYemoh8yeBHem1BCbU2vO3xN_29AfDNGoS3rkmDli-XvB22l0KSGVQwosU5Q%3D&authuser=0&page=2



#|%%--%%| <blQVch9jTm|KgCzvSQZOG>


data = requests.get(url_)

#|%%--%%| <KgCzvSQZOG|Q70GCcYlNZ>

data_a = data.text[4:]

#|%%--%%| <Q70GCcYlNZ|400FspaFQd>

print(data.text[:4])

#|%%--%%| <400FspaFQd|EfjD9vguRj>

print(json.loads(data_a))


#|%%--%%| <EfjD9vguRj|bQdEJY3vDm>

# this function convert from text to json format in each pages

# https://drive.google.com/file/d/1Nha1X48oIhLvz4qvgWJVqvK0w94u8ptI/view
def drive_page_to_json(**kwargs):
    # ck = kwargs.get("ck")
    # ds = kwargs.get("ds")
    # authuser = kwargs.get("authuser")
    page = kwargs.get("page")
    # url = kwargs.get("url")
    # url_ = f"https://drive.google.com/viewer2/prod-03/presspage?ck={ck}&ds={ds}&authuser={authuser}&page={page}"
    url_ = f"https://drive.google.com/viewer2/prod-03/presspage?ck=drive&ds=APznzaZtuM1mjnWBkoHQuv0P6A5Zv4TMmrvgNeEwVYdSIPbg3_EYu8uTStHC8knRAmTA6RhrzPTjA89co5IHS7_MbFHBP1F7-l3dG5kaPASnurFYqiH7xklzWRhC2ad8sPteVg7VZ6qj-7zJIM74DhoHGZhrRI5xgWxekS_FIkvCAK14_1M3A08cgUwVbMh6uQDFx39z-mFF-KFV9Eoy2iJVt9R2tGfpyT3pZ1VQY2XA0eNmOcvJy-Npi1msOl4jBJqheLuj19OU0VCWDa0ur4U2Cu7q54n2EN6EPe9Rv0u08joZnMBNAWjxRM9QqbuBmTbkFQxzKyBMTHrGLkFfanLMRMCv-7wkuP1_JeIRV3We8shNEOsJkqpSwIYJYemoh8yeBHem1BCbU2vO3xN_29AfDNGoS3rkmDli-XvB22l0KSGVQwosU5Q%3D&authuser=0&page={page}"


    print(url_)
    data = requests.get(url_).text[4:]
    print(data)
    return json.loads(data)
    



#|%%--%%| <bQdEJY3vDm|KSlX7ofJAl>

pages = 646


for i in range(1, pages + 1):
    with open(f"pages/{i}.json", "a") as f:
        x= json.dumps(drive_page_to_json(ck=ck, ds=ds, authuser=0, page=i))
        f.write(x)

# print()


#|%%--%%| <KSlX7ofJAl|gcI7JrYeft>
r"""°°°
This script for merage json with pdf images


°°°"""
#|%%--%%| <gcI7JrYeft|dwYqJMzyz9>

# # pip install PyMuPDF reportlab
# import fitz  # PyMuPDF
# import json
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4

# # Step 1: Extract images from the PDF
# def extract_images_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     images = []
#     for i in range(len(doc)):
#         for img in doc.get_page_images(i):
#             xref = img[0]
#             pix = fitz.Pixmap(doc, xref)
#             if pix.n < 5:       # this is GRAY or RGB
#                 pix.writePNG(f"page_{i + 1}.png")
#                 images.append(f"page_{i + 1}.png")
#             else:               # CMYK: convert to RGB first
#                 pix = fitz.Pixmap(fitz.csRGB, pix)
#                 pix.writePNG(f"page_{i + 1}.png")
#                 images.append(f"page_{i + 1}.png")
#             pix = None
#     return images

# # Step 2: Read text from the JSON file
# def read_text_from_json(json_path):
#     with open(json_path, 'r') as file:
#         data = json.load(file)
#     return data

# # Step 3: Combine images and text into a new PDF
# def create_new_pdf(images, texts, output_path):
#     c = canvas.Canvas(output_path, pagesize=A4)
#     width, height = A4
#     for i, image_path in enumerate(images):
#         c.drawImage(image_path, 0, 0, width=width, height=height)
#         c.setFont("Helvetica", 12)
#         text = texts.get(str(i + 1), "")  # Get text for the page, default to empty if not found
#         text_object = c.beginText(40, height - 40)
#         text_object.textLines(text)
#         c.drawText(text_object)
#         c.showPage()
#     c.save()

# # Usage example
# pdf_path = "your_pdf_file.pdf"
# json_path = "your_text_file.json"
# output_path = "output.pdf"

# images = extract_images_from_pdf(pdf_path)
# texts = read_text_from_json(json_path)
# create_new_pdf(images, texts, output_path)

