import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()


class AnylyzeService:
    def __init__(
        self, endpoint: str = f"{os.getenv('BACKEND_URL')}/analyze", timeout=120
    ):
        self.endpoint = endpoint
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def analyze(self, genius_artist_name: str, genius_song_name: str) -> dict:
        async with self.session.post(
            self.endpoint,
            json={
                "genius_artist_name": genius_artist_name,
                "genius_song_name": genius_song_name,
            },
        ) as resp:
            if resp.status != 200:
                raise Exception(await resp.text())
            return await resp.json()
