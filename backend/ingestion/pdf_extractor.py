from pathlib import Path 
import pymupdf

def extract_pdf(pdf_path: str) -> list[dict]:
    path = Path(pdf_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported")
    
    pages = []

    with pymupdf.open(path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text", sort=True).strip()

            pages.append({
                "page": page_number,
                "text": text,
                "char_count": len(text)
            })

        return pages

