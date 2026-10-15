from backend.ingestion.pdf_extractor import extract_pdf_text

pdf_path = "data/sample_docs/postgresql_manual.pdf"

pages = extract_pdf_text(pdf_path,max_pages = 50)

for page in pages:
    if page["page_number"] in [40,41,42]:
        print(f"\n{'=' * 50}")
        print(f"Page: {page['page_number']}")
        print(f"Charcters: {len(page['text'])}")
        print("=" * 50)
        print(page["text"][:1500])