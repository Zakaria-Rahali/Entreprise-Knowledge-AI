def chunk_pages(pages: list[dict], chunk_size: int=250, overlap: int=40) -> list[dict]:
    
    if chunk_size <= 0 or not 0 <= overlap < chunk_size:
        raise ValueError("Invalid chunk size or overlap")

    chunks = []

    for page in pages:
        words = page["text"].split()
        step = chunk_size - overlap

        for start in range(0, len(words), step):
            chunk_words = words[start:start + chunk_size]

            if not chunk_words:
                continue

            chunks.append({
                "page": page["page"],
                "text": " ".join(chunk_words),
                "word_count": len(chunk_words)
            })

            if start + chunk_size >= len(words):
                break
            
    return chunks
