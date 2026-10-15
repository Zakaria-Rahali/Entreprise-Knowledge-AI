import pymupdf 

pdf_path = "data/sample_docs/postgresql_manual.pdf"

with pymupdf.open(pdf_path) as doc:

    page = doc[41]

    words = page.get_text("words",sort=True)

    for i, word in enumerate(words):
        if "andit" in word[4] or word[4]=="and":
            print("\nCURRENT WORD:", word)

            print("NEIGHBORING WORDS:")

            for neighbor in words[max(0, i-2):i+4]:
                print(
                    f"Text: {neighbor[4]:15} "
                    f"x0: {neighbor[0]:.2f} "
                    f"x1: {neighbor[2]:.2f}"
                )