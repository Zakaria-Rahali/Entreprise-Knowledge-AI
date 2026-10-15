
import pymupdf

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:
    page = doc[41]

    text = page.get_text("text", sort=True)

    print("Correct spacing:", "and it" in text)
    print("Missing spacing:", "andit" in text)

    # Display the raw Python representation
    position = text.find("hard and")

    if position != -1:
        fragment = text[position:position + 40]

        print("Fragment:", repr(fragment))
        print("Character codes:", [ord(c) for c in fragment[:15]])
