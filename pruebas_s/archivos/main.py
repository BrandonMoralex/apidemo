from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Rutas para subir imágenes y PDF
IMAGES_DIR = "static/images"
PDF_DIR = "static/pdf"

# Función para guardar un archivo en una carpeta específica
def save_file(file, folder):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

@app.post("/upload/images/")
async def upload_images(files: list[UploadFile]):
    for file in files:
        save_file(file, IMAGES_DIR)
    return {"message": "Imagenes subidas exitosamente, gracias"}

@app.post("/upload/pdf/")
async def upload_pdf(files: list[UploadFile]):
    for file in files:
        save_file(file, PDF_DIR)
    return {"message": "PDFs subidos exitosamente, gracias"}

@app.get("/")
async def main():
    content = """
    <body>
    <h1>Subir Imágenes</h1>
    <form action="/upload/images/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" accept="image/*" multiple>
    <input type="submit" value="Subir Imágenes">
    </form>
    
    <h1>Subir PDFs</h1>
    <form action="/upload/pdf/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" accept=".pdf" multiple>
    <input type="submit" value="Subir PDFs">
    </form>
    </body>
    """
    return HTMLResponse(content=content)