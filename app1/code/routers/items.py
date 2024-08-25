from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{item_id}",
            tags=["items"])
async def read_item(item_id):
    return {"item_id": item_id}
