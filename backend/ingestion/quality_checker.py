import pymupdf 

def check_pdf_quality(pdf_path: str):
    page_results = []

    with pymupdf.open(pdf_path) as document:
        for page_index, page in enumerate(document):

            text = page.get_text("text")
            char_count = len(text.strip())

            if char_count == 0:
                status = "EMPTY"
            elif char_count < 100:
                status = "LOW_TEXT"
            else:
                status = "OK"

            page_results.append({
                "page_number": page_index + 1,
                "characters": char_count,
                "status": status
            })

    return page_results