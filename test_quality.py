from backend.ingestion.quality_checker import check_pdf_quality

pdf_path = "data/sample_docs/postgresql_manual.pdf"

results = check_pdf_quality(pdf_path)

empty_pages = [
    page for page in results
    if page["status"] == "EMPTY"
]

low_text_pages = [
    page for page in results
    if page["status"] == "LOW_TEXT"
]

average_chars = sum(
    page["characters"] for page in results
) / len(results)

print(f"Total pages: {len(results)}")
print(f"Average characters per page: {average_chars:.0f}")
print(f"Empty pages: {len(empty_pages)}")
print(f"Low-text pages: {len(low_text_pages)}")

print("\nFirst 10 flagged pages:")

for page in (empty_pages + low_text_pages)[:10]:
    print(
        f"Page {page['page_number']} | "
        f"{page['characters']} characters | "
        f"{page['status']}"
    )