import streamlit as st
from PIL import Image

# Load assets
statue = Image.open("assets/statue.png")
logo = Image.open("assets/logo.png")

# Streamlit page setup
st.set_page_config(
    page_title="Facebook Connect Yola",
    page_icon="🎉",
    layout="centered"
)

# Custom CSS for vibe
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77);
        color: #f0f0f0;
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background: transparent;
    }
    .stButton button {
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
    }
    .primary-btn {
        background-color: #1b263b !important;
        color: white !important;
    }
    .primary-btn:hover {
        background-color: #415a77 !important;
        color: #fff !important;
    }
    .secondary-btn {
        background-color: transparent !important;
        border: 2px solid #4cc9f0 !important;
        color: #4cc9f0 !important;
    }
    .secondary-btn:hover {
        background-color: #4cc9f0 !important;
        color: white !important;
    }
    .card {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Logo + Hero Section
st.image(logo, width=120)
st.title("🎉 Facebook Connect Yola")
st.subheader("Everyone is invited – guys & ladies 🤝")

# Statue visual
st.image(statue, use_column_width=True)

# Event Highlights
st.markdown("## 🌟 Event Highlights")
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'>🎶 DJ Atom bringing the vibes</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🍔 Food & Drinks</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>🎮 Games & Fun</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🎭 Culture & Networking</div>", unsafe_allow_html=True)

# Mars/Venus Toggle
gender = st.radio("Who are you booking for?", ["♂️ Men", "♀️ Ladies"])

# Booking Buttons
st.markdown("### 📌 Secure Your Spot")
c1, c2 = st.columns(2)
with c1:
    if st.button("🎟️ Book Your Spot", key="book", help="Reserve your seat at the event"):
        st.success("✅ Spot booked! See you at the event 🎉")
with c2:
    if st.button("ℹ️ Learn More", key="learn", help="More details coming soon"):
        st.info("📅 Event details: Coming Soon!")

# Footer
st.markdown("---")
st.caption("🌍 Facebook Connect Yola – Celebrating Culture & Community")
