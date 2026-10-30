import pymupdf
from pathlib import Path

pdf_path = "data/sample_docs/postgresql_manual.pdf"
output_dir = Path("data/validation")
output_dir.mkdir(parents=True, exist_ok=True)

pages_to_check=[1404, 1254, 2897]

with pymupdf.open(pdf_path) as document:
    for page_number in pages_to_check:
        page = document[page_number - 1]

        # save extracted text
        text = page.get_text("text", sort=True)

        (output_dir / f"page_{page_number}.txt").write_text(
            text,
            encoding="utf-8"
        )

        pix = page.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5))
        pix.save(str(output_dir / f"page_{page_number}.png"))

        print(f"Saved page {page_number}")

