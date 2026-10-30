import pymupdf

from backend.ingestion.structure_extractor import (
    extract_structured_page,
    merge_paragraph_lines,
    attach_section_metadata
)

pdf_path = "data/sample_docs/postgresql_manual.pdf"

state = {
    "chapter": None,
    "section": None
}

with pymupdf.open(pdf_path) as document:
    for page_index in range(41,44):
        page = document[page_index]

        elements = extract_structured_page(page)
        merged = merge_paragraph_lines(elements)

        structured = attach_section_metadata(
            merged,
            page_number = page_index + 1,
            state = state
        )

        print(f"\n{'=' * 45}")
        print(f"PDF PAGE {page_index + 1}")
        print(f"{'=' * 45}\n")

        for item in structured[:2]:
            print(f"Chapter: {item['chapter']}")
            print(f"Section: {item['section']}")
            print(f"Text: {item['text'][:90]}")
            print()