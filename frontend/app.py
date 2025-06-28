import streamlit as st
import requests
from PIL import Image
import io

# ========== CONFIGURATION ==========
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Garbage Classifier", page_icon="🗑️", layout="centered")

# ========== STYLING ==========
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        color: #2E8B57;
        margin-bottom: 0.3em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #444;
        margin-bottom: 1.5em;
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #888;
        margin-top: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown('<div class="title">🧠 Garbage Image Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and let the AI predict the type of waste</div>', unsafe_allow_html=True)

# ========== IMAGE UPLOAD ==========
uploaded_file = st.file_uploader("📤 Upload a Garbage Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Show preview
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Send image to API
    with st.spinner("🧠 Analyzing..."):
        response = requests.post(
            API_URL,
            files={"file": uploaded_file.getvalue()}
        )
    
    if response.status_code == 200:
        result = response.json()
        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        else:
            st.success(f"✅ Predicted Class: **{result['prediction'].capitalize()}**")
            st.info(f"🎯 Confidence: **{result['confidence']}%**")
    else:
        st.error("Something went wrong. Please try again.")

# ========== FOOTER ==========
st.markdown('<div class="footer">Built with ❤️ using FastAPI & Streamlit</div>', unsafe_allow_html=True)
