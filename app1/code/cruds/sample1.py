from sqlalchemy import asc
from models.model.sample1 import Sample1
from sqlalchemy.orm import Session


def list(db: Session):
    try:
        rows = db.query(Sample1)
        rows.order_by(asc("id"))
    except Exception as e:
        # Logger
        raise e
    return rows.all()


def get(db: Session, id: int):
    try:
        row = db.query(Sample1).filter(Sample1.id == id)
    except Exception as e:
        # Logger
        raise e
    return row.first()

