from fastapi import APIRouter, HTTPException
from app.db import database, notes, NoteIn, NoteOut

router = APIRouter()

@router.post("/data", response_model=NoteOut)
async def create_note(note: NoteIn):
    query = notes.insert().values(title=note.title, content=note.content)
    note_id = await database.execute(query)
    return {**note.dict(), "id": note_id}

@router.get("/data", response_model=list[NoteOut])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)
