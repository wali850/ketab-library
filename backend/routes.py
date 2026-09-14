from fastapi import APIRouter, Query

from services.book_search import search_openlibrary


router = APIRouter()


@router.get("/search")
async def search_books(
    q: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1, le=50),
):
    books = await search_openlibrary(q, limit)

    return {
        "query": q,
        "count": len(books),
        "books": books,
    }
