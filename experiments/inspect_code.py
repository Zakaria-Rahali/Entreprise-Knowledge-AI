import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:
    page = doc[42]  # PDF page 43

    blocks = page.get_text("dict", sort=True)["blocks"]

    for block in blocks:
        if block["type"] != 0:
            continue

        for line in block["lines"]:
            text = "".join(
                span["text"] for span in line["spans"]
            ).strip()

            if "createdb" not in text.lower():
                continue

            print(f"\nTEXT: {text}")

            for span in line["spans"]:
                print(
                    f"Font: {span['font']} | "
                    f"Size: {span['size']:.1f} | "
                    f"Text: {span['text']!r}"
                )
