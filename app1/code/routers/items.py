from fastapi import APIRouter, Depends
from models.database import Session, get_db
from fastapi.responses import JSONResponse
import cruds.sample1
router = APIRouter()

@router.get("/items/",
            tags=["items"])
async def get_items(db: Session = Depends(get_db)):
    hoge = cruds.sample1.list(db)
    return {}

@router.get("/items/{item_id}",
            tags=["items"])
async def read_item(item_id: int, db: Session = Depends(get_db)):
    hoge = cruds.sample1.get(db, item_id)
    if hoge is None:
        return JSONResponse(content="", status_code=404)
    return {"item_name": hoge.name}
