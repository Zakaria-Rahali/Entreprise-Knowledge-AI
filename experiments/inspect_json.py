
import json

with open(
    "data/postgresql_structured.json",
    encoding="utf-8"
) as file:
    records = json.load(file)

for record in records:
    if record["type"] == "code":
        print(f"\n[CODE] Page {record['page']}")
        print(repr(record["text"]))
