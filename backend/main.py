import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from .services.genius_client import GeniusClient
from .llm.analysis import interpret_lyrics

load_dotenv()
app = FastAPI()
genius = GeniusClient(os.getenv("GENIUS_API_TOKEN"))


class AnalyzeRequest(BaseModel):
    genius_artist_name: str
    genius_song_name: str


class AnalyzeResponse(BaseModel):
    summary: str
    line_explanations: dict


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    try:
        lyrics = await genius.fetch_lyrics(req.genius_artist_name, req.genius_song_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка Genius API: {e}")
    result = await interpret_lyrics(
        req.genius_song_name, req.genius_artist_name, lyrics
    )
    return result
