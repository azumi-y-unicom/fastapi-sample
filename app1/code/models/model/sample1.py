from sqlalchemy import Column, BigInteger, SmallInteger, String
from app1.code.models.database import Base


class Sample1(Base):
    __tablename__ = 'sample1'

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    description = Column("description", String)
    flag = Column("flag", SmallInteger, nullable=False)
