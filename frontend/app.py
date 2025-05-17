import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = f"{os.getenv('BACKEND_URL')}/analyze"

st.title("🎵 Genius Lyrics Decoder")

artist = st.text_input("Вставьте имя исполнителя")
song_name = st.text_input("Вставьте название песни")

if st.button("Анализировать") and artist and song_name:
    with st.spinner("Получаем текст и генерируем трактовки..."):
        resp = requests.post(
            ENDPOINT, json={"genius_artist_name": artist, "genius_song_name": song_name}
        )
        if resp.status_code == 200:
            data = resp.json()
            st.subheader("Краткий обзор")
            st.write(data["summary"])
            st.subheader("Трактовки строк")
            for line, expl in data["line_explanations"].items():
                st.markdown(f"> {line}  \n{expl}")
        else:
            st.error(f"Ошибка: {resp.text}")
