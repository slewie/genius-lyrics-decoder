import streamlit as st

from service.analyze_service import AnylyzeService


async def main():
    st.title("🎵 Genius Lyrics Decoder")

    artist = st.text_input("Вставьте имя исполнителя")
    song_name = st.text_input("Вставьте название песни")

    if st.button("Анализировать") and artist and song_name:
        with st.spinner("Получаем текст и генерируем трактовки..."):
            async with AnylyzeService() as service:
                data = await service.analyze(artist, song_name)
                st.subheader("Краткий обзор")
                st.write(data["summary"])


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
