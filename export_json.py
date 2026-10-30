import json
from pathlib import Path
import pymupdf

from backend.ingestion.structure_extractor import(
    extract_structured_page,
    merge_paragraph_lines,
    attach_section_metadata
)

pdf_path = Path("data/sample_docs/postgresql_manual.pdf")
output_path = Path("data/postgresql_structured.json")

state = {
    "chapter": None,
    "section": None
}

paragraphs = []

with pymupdf.open(pdf_path) as document:

    for page_index in range(41,44):
        page = document[page_index]

        elements = extract_structured_page(page)
        merged = merge_paragraph_lines(elements)

        structured = attach_section_metadata(
            merged,
            page_number=page_index + 1,
            state=state
        )

        paragraphs.extend(structured)

output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        paragraphs,
        file,
        ensure_ascii=False,
        indent=2
    )

print(f"Exported {len(paragraphs)} paragraphs")
print(f"Saved to: {output_path}")