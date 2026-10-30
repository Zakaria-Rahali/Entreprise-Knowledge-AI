import random

from backend.ingestion.quality_checker import check_pdf_quality

pdf_path = "data/sample_docs/postgresql_manual.pdf"

results = check_pdf_quality(pdf_path)

normal_pages = [
    result["page_number"]
    for result in results
    if result["status"] == "OK"
]

random.seed(42)

regions = [normal_pages[i::10] for i in range(10)]

sample = []

for region in regions:
    sample.extend(random.sample(region, k=2))

sample.sort()

print("Selected pages:")
print(sample)

