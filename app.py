import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем .env из текущей папки
load_dotenv()  # автоматически ищет файл .env в той же папке, что и app.py

# Получаем ключ
api_key = os.getenv("OPENAI_API_KEY")

# Проверка наличия ключа
if not api_key:
    st.error("API-ключ OpenAI не найден! Проверь файл .env")
    st.stop()

# Инициализация клиента OpenAI
client = OpenAI(api_key=api_key)

# Интерфейс приложения
st.set_page_config(page_title="StudyGenie", page_icon="🤖")
st.title("StudyGenie 🤖")
st.write("Твой AI-репетитор. Введи тему и получи объяснение простыми словами.")

topic = st.text_input("Введите тему:")

if st.button("Объяснить тему"):
    if not topic.strip():
        st.warning("Пожалуйста, введите тему.")
    else:
        with st.spinner("Генерирую объяснение..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Ты дружелюбный репетитор, который объясняет сложные темы простыми словами."},
                        {"role": "user", "content": f"Объясни тему: {topic} простыми словами."}
                    ],
                    temperature=0.7
                )

                explanation = response.choices[0].message.content
                st.success("Готово!")
                st.write(explanation)

            except Exception as e:
                st.error(f"Произошла ошибка: {e}")

