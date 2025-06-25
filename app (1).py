import streamlit as st
import random

# ---------- SETUP ---------- #
st.set_page_config(page_title="Kuis Daerah Indonesia", page_icon="📍", layout="centered")
st.title("🌍 Kuis: Seberapa Kenal Kamu dengan Daerah di Indonesia?")
st.write("Jawablah pertanyaan berikut dan lihat seberapa hebat pengetahuanmu tentang daerah-daerah di Indonesia!")

# ---------- PERTANYAAN ---------- #
questions = [
    {
        "question": "Apa ibu kota provinsi Jawa Tengah?",
        "options": ["Semarang", "Surakarta", "Yogyakarta"],
        "answer": "Semarang"
    },
    {
        "question": "Pulau manakah yang paling besar di Indonesia?",
        "options": ["Sumatera", "Kalimantan", "Sulawesi"],
        "answer": "Kalimantan"
    },
    {
        "question": "Suku Minangkabau berasal dari provinsi mana?",
        "options": ["Sumatera Utara", "Sumatera Barat", "Riau"],
        "answer": "Sumatera Barat"
    },
    {
        "question": "Danau Toba terletak di provinsi?",
        "options": ["Sumatera Utara", "Jambi", "Aceh"],
        "answer": "Sumatera Utara"
    },
    {
        "question": "Apa nama rumah adat dari Toraja?",
        "options": ["Tongkonan", "Joglo", "Gadang"],
        "answer": "Tongkonan"
    }
]

random.shuffle(questions)

# ---------- SKOR ---------- #
skor = 0

# ---------- FORMULIR ---------- #
user_answers = []
with st.form("quiz_form"):
    for i, q in enumerate(questions):
        answer = st.radio(f"{i+1}. {q['question']}", q["options"], key=i)
        user_answers.append(answer)

    submitted = st.form_submit_button("📍 Cek Skor Saya!")

# ---------- HASIL ---------- #
if submitted:
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            skor += 1

    st.success(f"🎉 Skor kamu: {skor} dari {len(questions)} pertanyaan!")

    if skor == len(questions):
        st.balloons()
        st.info("Keren! Kamu sangat mengenal daerah-daerah di Indonesia!")
    elif skor >= 3:
        st.info("Lumayan! Tapi masih bisa belajar lebih dalam lagi tentang Indonesia!")
    else:
        st.warning("Yuk pelajari lebih banyak tentang kekayaan daerah Indonesia!")
