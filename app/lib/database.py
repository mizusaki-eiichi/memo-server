from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import Settings


settings = Settings()


SQLALCHEMY_DATABASE_URL = "{engine}://{user}:{password}@{host}:{port}/{database}".format(
    engine=settings.databases["ENGINE"],
    user=settings.databases["USER"],
    password=settings.databases["PASSWORD"],
    host=settings.databases["HOST"],
    port=settings.databases["PORT"],
    database=settings.databases["DATABASE"],
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
