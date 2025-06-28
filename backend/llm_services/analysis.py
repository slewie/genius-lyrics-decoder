from typing import Dict
from langchain_core.output_parsers import StrOutputParser
from utils.llm import llm
from utils.logger import logger
from .prompts import summarize_template, collect_artist_info_template


async def collect_artist_info(artist_name: str):
    # TODO: добавить кеширование
    artist_info_chain = collect_artist_info_template | llm | StrOutputParser()
    return await artist_info_chain.ainvoke({"artist_name": artist_name})


async def generate_summary(lyrics: str, artist_info: str):
    summary_chain = summarize_template | llm | StrOutputParser()
    return await summary_chain.ainvoke({"lyrics": lyrics, "artist_info": artist_info})


async def interpret_lyrics(song_name: str, artist_name: str, lyrics: str) -> Dict:
    """
    1) Генерируем сводку по всему тексту
    2) По-строчные трактовки (берём первые 10 непустых)
    """

    artist_info = await collect_artist_info(artist_name)
    logger.info(f"Artist info: {artist_info}")
    summary = await generate_summary(lyrics, artist_info)
    logger.info(f"Summary: {summary}")

    return {"summary": summary}
