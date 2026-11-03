import hashlib


def enrich_chunks(chunks: list[dict], document_id: str) -> list[dict]:
    enriched = []

    for index, chunk in enumerate(chunks):
        raw_id = f"{document_id}:{index}:{chunk['text']}"

        chunk_id = hashlib.sha256(
            raw_id.encode("utf-8")
        ).hexdigest()

        enriched.append({
            **chunk,
            "chunk_id": chunk_id,
            "document_id": document_id,
            "chunk_index": index
        })

    return enriched
