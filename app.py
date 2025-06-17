import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Your Buddy 🌼", page_icon="💛")

# Title and Welcome
st.title("Hey there, amazing soul! 💛")
st.write("Welcome to *Your Buddy*, a little safe space on the internet 🌸")

# Mood Selector
mood = st.selectbox("How are you feeling today?", ["🙂 Okay", "😔 Sad", "😄 Happy", "😣 Stressed", "😩 Anxious", "❤️ Grateful"])

# Uplifting Responses
responses = {
    "🙂 Okay": "It's okay to feel just okay. Small steps matter too 🌿",
    "😔 Sad": "You're not alone. This too shall pass. Sending you a warm hug 🤗",
    "😄 Happy": "Yayy! Keep spreading that joy 🌞",
    "😣 Stressed": "Take a deep breath... You're doing your best and that's enough 💆",
    "😩 Anxious": "You're stronger than the thoughts in your head. Breathe and be kind to yourself 🌬️",
    "❤️ Grateful": "Gratitude unlocks joy. Cherish this moment ✨"
}

st.write(responses[mood])

# Random Quote Button
quotes = [
    "You’ve survived 100% of your bad days. You’re doing great! 🌼",
    "Self-care is not selfish. 🌸",
    "Your feelings are valid, even when you don’t understand them 💖",
    "Be proud of how far you've come 🦋",
    "You are enough. Always have been, always will be 💛"
]

if st.button("I need a little positivity ✨"):
    st.success(random.choice(quotes))

# Footer
st.write("---")
st.caption("With love, from Your Buddy 💫")
