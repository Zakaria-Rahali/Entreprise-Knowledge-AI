
import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:

    for page_index in [42, 43]:
        page = doc[page_index]

        print(f"\n--- PDF PAGE {page_index + 1} ---")
        print(f"Page height: {page.rect.height:.1f}")

        blocks = page.get_text("dict", sort=True)["blocks"]

        for block in blocks:
            if block["type"] != 0:
                continue

            text = " ".join(
                span["text"]
                for line in block["lines"]
                for span in line["spans"]
            ).strip()

            if not text:
                continue

            print(
                f"Y-position: {block['bbox'][1]:.1f} | "
                f"Text: {text[:90]}"
            )

            # Only inspect blocks near the top
            if block["bbox"][1] > 120:
                break
