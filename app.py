 
import os
import streamlit as st
from PIL import Image

# Directories
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def load_image(filename):
    path = os.path.join(ASSETS_DIR, filename)
    return Image.open(path)

# Load images
statue = load_image("statue.png")
logo = load_image("logo.png")
bg = load_image("bg.png")

# --- UI ---
st.set_page_config(page_title="Facebook Connect Yola", page_icon="🎉", layout="centered")

st.image(logo, use_column_width=True)
st.title("🎉 Facebook Connect Yola")
st.subheader("Everyone is invited — Guys & Ladies")

st.image(statue, caption="Cultural Yola Statue", use_column_width=True)

# Gender toggle
gender = st.radio("Choose your vibe:", ["♂️ Men", "♀️ Women", "🌍 Everyone"])

# Booking section
st.header("📅 Event Info")
st.write("Coming Soon — Stay tuned for date & time!")
st.write("Featuring: DJ Atom 🎶 | Food 🍲 | Drinks 🍹 | Games 🎲")

if st.button("✅ Book Your Spot"):
    st.success("Thanks for booking! You selected: " + gender)

st.image(bg, use_column_width=True, caption="Event Vibes Background")
