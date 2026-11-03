from backend.ingestion.chunk_metadata import enrich_chunks

def test_enrich_chunks():
    chunks = [
        {"page": 1, "text": "PostgreSQL installation"},
        {"page": 2, "text": "Creating a database"}
    ]

    result = enrich_chunks(chunks,"postgresql_18_6")
    repeated = enrich_chunks(chunks, "postgresql_18_6")

    assert len(result) == 2
    assert result[0]["document_id"] == "postgresql_18_6"
    assert result[0]["chunk_index"] == 0
    assert result[0]["page"] == 1

    assert result[0]["chunk_id"] != result[1]["chunk_id"]
    assert result[0]["chunk_id"] == repeated[0]["chunk_id"]

    