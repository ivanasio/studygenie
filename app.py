import os
import streamlit as st
from openai import OpenAI

api_key = st.secrets["OPENAI_KEY"]

if not api_key:
    st.error("OPENAI_KEY не найден. Добавь его в Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("StudyGenie 🤖")

# Ввод темы пользователем
topic = st.text_input("Введите тему:")

if topic:
    if st.button("Объяснить тему"):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Ты дружелюбный репетитор."},
                    {"role": "user", "content": f"Объясни тему: {topic} простыми словами."}
                ]
            )
            # Вывод ответа AI
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Произошла ошибка при запросе к OpenAI: {e}")

