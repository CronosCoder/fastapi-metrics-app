from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from databases import Database
from app.config import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", String(1000))
)

engine = create_engine(DATABASE_URL.replace("postgres://", "postgresql://"))
metadata.create_all(engine)

from pydantic import BaseModel

class NoteIn(BaseModel):
    title: str
    content: str

class NoteOut(NoteIn):
    id: int
