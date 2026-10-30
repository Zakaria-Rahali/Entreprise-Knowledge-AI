import pymupdf

from backend.ingestion.quality_checker import check_pdf_quality

pdf_path = "data/sample_docs/postgresql_manual.pdf"

results = check_pdf_quality(pdf_path)

flagged = [
    result for result in results
    if result["status"] != "OK"
]

with pymupdf.open(pdf_path) as document:
    for result in flagged:
        page_number = result["page_number"]
        page = document[page_number - 1]

        text = page.get_text("text").strip()

        print(f"\n{'=' * 50}")
        print(f"PAGE: {page_number}")
        print(f"CHARACTERS: {result['characters']}")
        print(f"TEXT: {text[:200]!r}")