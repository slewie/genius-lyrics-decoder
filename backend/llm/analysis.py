from typing import Dict
from tqdm import tqdm
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini-2024-07-18",
    openai_api_key="unused",
    openai_api_base="https://api.llm7.io/v1",
    temperature=0.85,
    max_tokens=500,
)


# 2) Готовим два Prompt-шаблона (в новых версиях input_variables не указываем)
summarize_template = ChatPromptTemplate.from_template(
    """Ты — музыкальный аналитик.
Дай краткий обзор основных тем и мотивов в этом тексте песни:

{lyrics}"""
)

explain_template = ChatPromptTemplate.from_template(
    """\
Ты — музыкальный аналитик. Объясни смысл следующей строки из песни {song_name}, исполнителя {artist_name}, дай возможные трактовки, будь лаконичен и краток(не больше пары предложений).
"{line}" """
)


explanation_chain = explain_template | llm


# Функция для батч-обработки
async def process_in_batches(
    lines: list[str], song_name: str, artist_name: str, batch_size=10
):
    line_explanations = {}

    for i in tqdm(range(0, len(lines), batch_size)):
        batch = lines[i : i + batch_size]
        inputs = [
            {"line": line, "song_name": song_name, "artist_name": artist_name}
            for line in batch
        ]

        # Отправляем батч асинхронно
        responses = await explanation_chain.abatch(inputs)

        for line, resp in zip(batch, responses):
            explanation = resp.content.strip()
            line_explanations[line] = explanation

    return line_explanations


async def interpret_lyrics(song_name: str, artist_name: str, lyrics: str, k: int = 1) -> Dict:
    """
    1) Генерируем сводку по всему тексту
    2) По-строчные трактовки (берём первые 10 непустых)
    """
    summary_chain = summarize_template | llm
    summary_resp = await summary_chain.ainvoke({"lyrics": lyrics})
    summary = summary_resp.content

    lines = []
    current_pair = []
    
    for line in lyrics.splitlines():
        line = line.strip()
        if line and not line.startswith("[") and not line.endswith("]"):
            current_pair.append(line)
            if len(current_pair) == k:
                lines.append("\n\n".join(current_pair))
                current_pair = []
    if current_pair:
        lines.append(current_pair[0])
    
    print(f"Processing {len(lines)} lines...")
    line_explanations = await process_in_batches(lines, song_name, artist_name)

    return {"summary": summary, "line_explanations": line_explanations}
