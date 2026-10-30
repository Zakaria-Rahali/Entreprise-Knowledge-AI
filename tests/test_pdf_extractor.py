from backend.ingestion.pdf_extractor import extract_pdf
import pytest

def test_pdf_extraction():
    pages = extract_pdf(
        "data/sample_docs/postgresql_manual.pdf"
    )

    assert len(pages) > 0
    assert pages[0]["page"] == 1
    assert all("text" in page for page in pages)
    assert all("char_count" in page for page in pages)

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        extract_pdf("nonexistent.pdf")

def test_invalid_extension(tmp_path):
    file_path = tmp_path/"document.txt"
    file_path.write_text("This is not a PDF.")

    with pytest.raises(ValueError):
        extract_pdf(str(file_path))