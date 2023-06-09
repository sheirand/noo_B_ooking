from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.pg_dsn

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
