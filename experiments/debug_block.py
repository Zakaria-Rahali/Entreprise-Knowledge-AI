
import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:
    page = doc[41]

    blocks = page.get_text("dict", sort=True)["blocks"]

    for block_index, block in enumerate(blocks):

        if block["type"] != 0:
            continue

        text = " ".join(
            span["text"]
            for line in block["lines"]
            for span in line["spans"]
        )

        if "If your site administrator" not in text:
            continue

        print(f"\nBLOCK {block_index}")
        print("=" * 60)

        for line in block["lines"]:
            for span in line["spans"]:
                print(
                    f"Font: {span['font']:20} "
                    f"Size: {span['size']:.1f} | "
                    f"Text: {span['text']}"
                )
