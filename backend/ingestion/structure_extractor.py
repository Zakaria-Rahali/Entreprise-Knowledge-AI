import pymupdf

def classify_block(font_size: float) -> str:
    if font_size >= 24:
        return 'chapter'

    elif font_size >= 18:
        return 'section'

    else:
        return 'paragraph'

def extract_structured_page(page):
    elements = []

    blocks = page.get_text("dict",sort=True)["blocks"]

    for block_index, block in enumerate(blocks):
        if block["type"] != 0:
            continue

        for line in block["lines"]:
            spans = [
                span for span in line["spans"]
                if span["text"].strip()
            ]

            if not spans:
                continue

            text = "".join(
                span["text"] for span in spans
            ).strip()

            font_size = max(
                span["size"] for span in spans
            )

            element_type = classify_block(font_size)

            elements.append({
                "type": element_type,
                "font_size": round(font_size, 1),
                "text": text,
                "block_id": block_index
            })

    return elements


def merge_paragraph_lines(elements):
    merged = []

    for element in elements:
        if (
            merged
            and element["type"] == "paragraph"
            and merged[-1]["type"] == "paragraph"
            and element["block_id"] == merged[-1]["block_id"]
        ):
            merged[-1]["text"] += " " + element["text"]

        else:
            merged.append(element.copy())

    return merged

def attach_section_metadata(elements, page_number):
    current_chapter = None
    current_section = None

    structured = []

    for element in elements:

        if element["type"] == "chapter":
            current_chapter = element["text"]
            current_section = None

        elif element["type"] == "section":
            current_section = element["text"]

        elif element["type"] == "paragraph":
            structured.append({
                "chapter": current_chapter,
                "section": current_section,
                "page": page_number,
                "text": element["text"]
            })
    return structured

