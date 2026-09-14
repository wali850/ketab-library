import httpx


async def search_openlibrary(query: str, limit: int = 10):
    url = "https://openlibrary.org/search.json"

    params = {
        "q": query,
        "limit": limit,
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    books = []

    for item in data.get("docs", []):
        books.append({
            "title": item.get("title"),
            "author": (item.get("author_name") or [None])[0],
            "language": (item.get("language") or [None])[0],
            "year": item.get("first_publish_year"),
            "cover_id": item.get("cover_i"),
            "openlibrary_key": item.get("key"),
        })

    return books
