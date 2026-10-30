import pymupdf

from backend.ingestion.quality_checker import check_pdf_quality

pdf_path = "data/sample_docs/postgresql_manual.pdf"

sample_pages = [
    122, 141, 158, 167, 446,
    478, 525, 572, 714, 1119,
    1144, 1199, 1254, 1404, 2181,
    2605, 2811, 2897, 3044, 3109
]

with pymupdf.open(pdf_path) as document:
    for page_number in sample_pages:
        page = document[page_number - 1]

        blocks = page.get_text("dict")["blocks"]

        text_blocks = sum(
            1 for block in blocks
            if block["type"] == 0
        )

        image_blocks = sum(
            1 for block in blocks
            if block["type"] == 1
        )

        text = page.get_text("text")

        print(
            f"Page {page_number:4} | "
            f"Characters: {len(text.strip()):5} | "
            f"Text blocks: {text_blocks:3} | "
            f"Image blocks: {image_blocks}"
        )
