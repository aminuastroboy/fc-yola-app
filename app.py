import streamlit as st
from pathlib import Path

# --- Page Config ---
st.set_page_config(
    page_title="Facebook Connect Yola",
    page_icon="🌍",
    layout="wide",
)

# --- Paths ---
BASE = Path(__file__).parent if "__file__" in locals() else Path(".")
IMG = BASE / "static" / "img"

# --- Custom CSS for Material vibes + Animations + Hover Effects ---
st.markdown("""
<style>
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #0A1D37, #008080, #00B8D9);
        background-size: 600% 600%;
        animation: gradientFlow 20s ease infinite;
        color: white;
    }

    .card {
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        backdrop-filter: blur(10px);
        animation: fadeInUp 1s ease forwards;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 12px 30px rgba(0,0,0,0.6), 0 0 20px rgba(0,184,217,0.6);
    }

    .title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease forwards;
    }

    .hero-img {
        animation: zoomIn 1.2s ease forwards;
        transition: transform 0.4s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .hero-img:hover {
        transform: scale(1.05);
    }

    .download-section {
        animation: fadeInUp 1s ease forwards;
    }

    .stRadio > div[role='radiogroup'] > label {
        font-size: 1.2rem;
        margin-right: 1.5rem;
        cursor: pointer;
    }

    .stDownloadButton button {
        border-radius: 12px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        background: linear-gradient(135deg, #008080, #00B8D9);
        border: none;
        transition: all 0.3s ease;
        color: white;
    }
    .stDownloadButton button:hover {
        background: linear-gradient(135deg, #00B8D9, #008080);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,184,217,0.5);
    }

    /* --- Background animation --- */
    @keyframes gradientFlow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* --- Animations --- */
    @keyframes fadeInUp {
        from {opacity:0; transform: translateY(40px);}
        to {opacity:1; transform: translateY(0);}
    }
    @keyframes fadeInDown {
        from {opacity:0; transform: translateY(-40px);}
        to {opacity:1; transform: translateY(0);}
    }
    @keyframes zoomIn {
        from {opacity:0; transform: scale(0.8);}
        to {opacity:1; transform: scale(1);}
    }
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<div class='title'>🌍 Facebook Connect Yola</div>", unsafe_allow_html=True)
st.image(IMG / "statue-hero.png", use_column_width=True, caption="Cultural Statue in Abstract Style", output_format="PNG")

# --- Event Highlights ---
st.markdown("### 🎉 Event Highlights")
cols = st.columns(4)

with cols[0]:
    st.markdown("<div class='card'>🎶 Music by DJ Atom</div>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<div class='card'>🍲 Foods</div>", unsafe_allow_html=True)
with cols[2]:
    st.markdown("<div class='card'>🍹 Drinks</div>", unsafe_allow_html=True)
with cols[3]:
    st.markdown("<div class='card'>🎲 Games</div>", unsafe_allow_html=True)

# --- Coming Soon Section ---
st.markdown("## ⏳ Coming Soon")
st.info("Everyone is invited — both guys and ladies! Stay tuned for date & time.")

# --- Logos Toggle Section ---
st.markdown("<div class='download-section'><h2>📥 Download Logo</h2></div>", unsafe_allow_html=True)

choice = st.radio(
    "Choose your logo version:",
    ("♂ Men", "♀ Women"),
    horizontal=True
)

if "Men" in choice:
    st.image(IMG / "logo-men-800.png", use_column_width=True)
    men_hr_path = IMG / "logo-men-4500.png"
    if men_hr_path.exists():
        with open(men_hr_path, "rb") as f:
            st.download_button(
                label="⬇ Download Men’s High-Res",
                data=f,
                file_name="fc_yola_logo_men.png",
                mime="image/png",
                key="dl_men_toggle"
            )
else:
    st.image(IMG / "logo-ladies-800.png", use_column_width=True)
    ladies_hr_path = IMG / "logo-ladies-4500.png"
    if ladies_hr_path.exists():
        with open(ladies_hr_path, "rb") as f:
            st.download_button(
                label="⬇ Download Ladies’ High-Res",
                data=f,
                file_name="fc_yola_logo_ladies.png",
                mime="image/png",
                key="dl_ladies_toggle"
)
