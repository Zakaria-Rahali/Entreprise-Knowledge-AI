import pymupdf 

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:

    page = doc[41]

    blocks = page.get_text("dict",sort=True)['blocks']

    for index, block in enumerate(blocks):
        if block["type"] != 0:
            continue

        lines = []

        for line in block["lines"]:
            text = "".join(
                span["text"] for span in line["spans"]
            )
            lines.append(text)

        block_text = "\n".join(lines)

        print(f"\n--- BLOCK {index} ---")
        print(f"Number of lines: {len(lines)}")
        print(f"Text: {block_text[:300]}")