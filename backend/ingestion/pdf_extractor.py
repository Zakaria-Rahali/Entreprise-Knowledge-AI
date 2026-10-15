import pymupdf

def extract_pdf_text(file_path: str, max_pages: int=3):
    extracted_pages = []

    with pymupdf.open(file_path) as document:

        for page_index in range(min(max_pages, len(document))):
            page = document[page_index]
            text = page.get_text("text", sort=True)

            extracted_pages.append({
                "page_number": page_index + 1,
                "text": text
            })

    return extracted_pages
