import pytest

from backend.ingestion.chunker import chunk_pages

def test_chunking_with_overlap():
    pages = [{
        "page": 1,
        "text": " ".join(f"word{i}" for i in range(10))
    }]

    chunks = chunk_pages(pages, chunk_size=6, overlap=2)

    assert len(chunks) == 2
    assert chunks[0]["word_count"] == 6
    assert chunks[1]["word_count"] == 6
    assert chunks[0]["text"].split()[-2:] == (
        chunks[1]["text"].split()[:2]
    )
    assert all(chunk["page"] == 1 for chunk in chunks)

def test_empty_page():
    assert chunk_pages([{"page": 1, "text": ""}]) == []

def test_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_pages(
            [{"page": 1, "text": "hello"}],
            chunk_size=10,
            overlap=10
        )