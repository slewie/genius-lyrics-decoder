import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from .services.genius_client import GeniusClient
from .llm_services.analysis import interpret_lyrics
from .models import AnalyzeRequest, AnalyzeResponse

load_dotenv()
app = FastAPI()
genius = GeniusClient(os.getenv("GENIUS_API_TOKEN"))


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


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("BACKEND_PORT", 8000)))
