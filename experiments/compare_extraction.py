import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:

    page = doc[41]

    blocks = page.get_text("blocks", sort=True)

    for index, block in enumerate(blocks[:8]):
        text = block[4]

        print(f"\n--- BLOCK {index} ---")
        print(text[:400])