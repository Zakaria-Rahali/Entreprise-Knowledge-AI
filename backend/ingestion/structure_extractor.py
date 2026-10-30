import pymupdf
import re

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

            if is_code_line(spans) and font_size < 18:
                element_type = "code"
            else:
                element_type = classify_block(font_size)

            elements.append({
                "type": element_type,
                "font_size": round(font_size, 1),
                "text": text,
                "block_id": block_index,
                "y_position": line["bbox"][1]
            })

    return elements



def merge_paragraph_lines(elements):
    merged = []

    for element in elements:
        if (
            merged
            and element["type"] in ("paragraph", "code")
            and element["type"] == merged[-1]["type"]
            and element["block_id"] == merged[-1]["block_id"]
        ):
            separator = (
                "\n" if element["type"] == "code" else " "
            )

            merged[-1]["text"] += separator + element["text"]

        else:
            merged.append(element.copy())

    return merged


def attach_section_metadata(elements, page_number, state):
    structured = []

    for element in elements:
        if element["type"] == "chapter":
            state["chapter"] = element["text"]
            state["section"] = None

        elif element["type"] == "section":
            state["section"] = element["text"]

        elif element["type"] in ("paragraph", "code"):
            if is_running_header(
                text=element["text"],
                y_position=element["y_position"],
                current_chapter=state["chapter"]
            ):
                continue

            structured.append({
                "type": element["type"],
                "chapter": state["chapter"],
                "section": state["section"],
                "page": page_number,
                "text": element["text"]
            })

    return structured

def is_running_header(text, y_position, current_chapter):
    if not current_chapter:
        return False

    # Example: "Chapter 1. Getting Started" -> "Getting Started"
    chapter_name = re.sub(
        r"^Chapter\s+\d+\.\s*",
        "",
        current_chapter
    ).strip()

    return (
        y_position < 50
        and text.strip() == chapter_name
    )


def is_code_line(spans):
    return all(
        "Courier" in span["font"]
        for span in spans
    )
