import streamlit as st
import random
import datetime

# --- Mood Data ---
mood_data = {
    "Happy": {
        "songs": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=KQetemT1sWc",
            "https://www.youtube.com/watch?v=HgzGwKwLmgM"
        ],
        "quote": "Happiness is not by chance, but by choice. – Jim Rohn",
        "color": "#FFF9C4",
        "emoji": "😊"
    },
    "Sad": {
        "songs": [
            "https://www.youtube.com/watch?v=RgKAFK5djSk",
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",
            "https://www.youtube.com/watch?v=J_ub7Etch2U"
        ],
        "quote": "Tears come from the heart and not from the brain. – Leonardo da Vinci",
        "color": "#E1BEE7",
        "emoji": "😢"
    },
    "Focused": {
        "songs": [
            "https://www.youtube.com/watch?v=hHW1oY26kxQ",
            "https://www.youtube.com/watch?v=WPni755-Krg",
            "https://www.youtube.com/watch?v=5qap5aO4i9A"
        ],
        "quote": "Focus on being productive instead of busy. – Tim Ferriss",
        "color": "#C8E6C9",
        "emoji": "🎯"
    },
    "Relaxed": {
        "songs": [
            "https://www.youtube.com/watch?v=2OEL4P1Rz04",
            "https://www.youtube.com/watch?v=eKFTSSKCzWA",
            "https://www.youtube.com/watch?v=1ZYbU82GVz4"
        ],
        "quote": "Almost everything will work again if you unplug it for a few minutes – including you. – Anne Lamott",
        "color": "#B3E5FC",
        "emoji": "🌿"
    }
}

# --- Streamlit App ---
st.set_page_config(page_title="Mood-Based Music & Quotes", layout="centered")
st.title("🎧 Mood-Based Music & Quote Recommender")

# Mood selection
mood = st.selectbox("How are you feeling today?", list(mood_data.keys()))
data = mood_data[mood]

# Set background color dynamically
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {data['color']};
            color: #333;
        }}
    </style>
""", unsafe_allow_html=True)

# Display emoji mood header
st.markdown(f"## {data['emoji']} You're feeling {mood} today")

# Display quote
st.subheader("💬 Motivational Quote")
st.info(data["quote"])

# Display current time
st.markdown(f"🕒 Current Time: {datetime.datetime.now().strftime('%I:%M %p')}")

# Display songs
st.subheader("🎵 Recommended YouTube Songs")
random.shuffle(data["songs"])
for url in data["songs"]:
    st.write(f"▶️ [Watch here]({url})")

# Add note-taking feature
st.subheader("📝 Quick Mood Journal")
note = st.text_area("Write your thoughts here (private, not saved)...")
if st.button("Clear Notes"):
    st.rerun()

st.markdown("---")
st.caption("Enjoy your mood and stay inspired ✨")


