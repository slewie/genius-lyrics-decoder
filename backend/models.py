from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    genius_artist_name: str
    genius_song_name: str


class AnalyzeResponse(BaseModel):
    summary: str
