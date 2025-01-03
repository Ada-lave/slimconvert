from fastapi .testclient import TestClient
from slimconvert.server import app

client = TestClient(app)

def test_max_input_file_size():
    response = client.post("/convert-docx", files={"file": ("large.docx", b" " * 1024 * 1024 * 11)})
    assert response.status_code == 422
    assert response.json() == "File too large"

def test_file_is_docx():
    response = client.post("/convert-docx", files={"file": ("test.txt", b"")})
    assert response.status_code == 422
    assert response.json() == "Invalid file type"