from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import random

import os


PRIMARY_KEY_NAME = "primary"
REPLICA_KEY_BASE = "replica_"
PRIMARY_DB_HOST = "postgres:5432"
PRIMARY_DB_DATABASE = "postgres"
PRIMARY_DB_USER = "root"
PRIMARY_DB_PASSWORD = "password"

# レプリカエンドポイント
REPLICA_DB_HOST_1 = "postgres:5433"
REPLICA_DB_DATABASE_1 = "postgres"


# カスタマイズSession
class DatabaseSession(Session):
    _name = None

    def get_bind(self):
        engine = None
        if self._name:
            engine = engines[self._name]
        elif self._flushing and self._transaction:
            engine = engines[PRIMARY_KEY_NAME]
        else:
            # engine = engines[random.choice(replica_keys)]
            engine = engines[PRIMARY_KEY_NAME]
        return engine

    def using_bind(self, name: str):
        session: DatabaseSession = DatabaseSession()
        vars(session).update(vars(self))
        session._name = name

        return session


DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('PASSWORD')


def primary_database_url():
    HOST = os.getenv('PRIMARY_DB_HOST')
    DATABASE = os.getenv('PRIMARY_DB_DATABASE')
    return f"postgresql+psycopg2://{DB_USER}:{PASSWORD}@{HOST}/{DATABASE}"


def replica_database_url():
    HOST = os.getenv('REPLICA_DB_HOST_1')
    DATABASE = os.getenv('REPLICA_DB_DATABASE_1')
    return f"postgresql+psycopg2://{DB_USER}:{PASSWORD}@{HOST}/{DATABASE}"


SQLALCHEMY_DATABASE_URL = primary_database_url()
print(SQLALCHEMY_DATABASE_URL)
engines = {
    PRIMARY_KEY_NAME: create_engine(
        SQLALCHEMY_DATABASE_URL
    )
}

replica_keys = []

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engines[PRIMARY_KEY_NAME]
)

Base = declarative_base() 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
