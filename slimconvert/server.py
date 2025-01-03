from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware 
from docx import Document
import tempfile
import os
import subprocess

MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 10)) * 1024 * 1024

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/convert-docx")
async def process_docx(
    file: UploadFile = File(...)
):
    if file.size > MAX_FILE_SIZE:
        return JSONResponse("File too large", 422) 
    
    if not file.filename.endswith(".docx"):
        return JSONResponse("Invalid file type", 422) 
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
    
   
    pdf_file_path = os.path.splitext(temp_file_path)[0] + ".pdf"
    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", temp_file_path, "--outdir", os.path.dirname(temp_file_path)])
    return FileResponse(
        pdf_file_path,
        filename=f"processed_{os.path.splitext(file.filename)[0]}.pdf",
        media_type="application/pdf",
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)