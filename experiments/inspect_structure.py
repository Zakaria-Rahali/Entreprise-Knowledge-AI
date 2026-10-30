import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:
    page = doc[41]

    blocks = page.get_text("dict")["blocks"]

    for block in blocks:
        if block["type"] != 0:
            continue

        for line in block["lines"]:
            for span in line["spans"]:
                text = span["text"].strip()

                if not text:
                    continue

                print(
                    f"Font size: {span['size']:.1f} |"
                    f"Font: {span['font']} |"
                    f"Text: {text[:100]}"
                )