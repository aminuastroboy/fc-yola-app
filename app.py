import streamlit as st
from PIL import Image
import os

# Path to assets folder
ASSETS_DIR = "assets"

def load_image(path):
    return Image.open(os.path.join(ASSETS_DIR, path))

# --- APP CONFIG ---
st.set_page_config(page_title="Facebook Connect Yola", page_icon="🌍", layout="wide")

# --- HERO SECTION ---
st.image(load_image("hero/statue.png"), use_column_width=True)

st.title("Facebook Connect Yola")
st.subheader("Everyone is invited — both guys and ladies 🎉")
st.markdown("---")

# --- TOGGLE SWITCH (Men/Women) ---
gender = st.radio("Choose your vibe:", ["Men", "Women"], horizontal=True)

if gender == "Men":
    st.image(load_image("logos/logo_mars.png"), width=120)
else:
    st.image(load_image("logos/logo_venus.png"), width=120)

st.markdown("---")

# --- EVENT CARDS ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image(load_image("icons/food.png"), width=80)
    st.caption("Food")

with col2:
    st.image(load_image("icons/drinks.png"), width=80)
    st.caption("Drinks")

with col3:
    st.image(load_image("icons/music.png"), width=80)
    st.caption("Music")

with col4:
    st.image(load_image("icons/games.png"), width=80)
    st.caption("Games")

with col5:
    st.image(load_image("icons/dj.png"), width=80)
    st.caption("DJ Atom")

st.markdown("---")

# --- COMING SOON FOOTER ---
st.info("📅 Event date & time: Coming Soon!")
st.success("✨ Join us and celebrate culture, music, and friendship in Yola.")
