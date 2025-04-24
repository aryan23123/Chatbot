from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import random

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
if google_api_key:
    genai.configure(api_key=google_api_key)
else:
    st.error("🔐 Google AI API key not found. Add it to `.env` as GOOGLE_API_KEY.")
    st.stop()

# --- Page Setup & Styling ---
st.set_page_config(page_title="👻 Paranormal Detector", page_icon="🧲", layout="wide")
st.markdown("""
    <style>
        html, body {
            background-color: #0a0a0a;
            color: #f0e6f6;
            font-family: 'Georgia', serif;
        }
        .stTextArea textarea {
            background-color: #1f1f2e;
            color: #e6e6fa;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #4b0082;
            color: #fff;
            font-weight: bold;
            border-radius: 6px;
            padding: 0.6rem 1.2rem;
        }
        .stButton > button:hover {
            background-color: #37005f;
        }
        h1, h2, h3 {
            color: #f7f3ff;
            text-shadow: 1px 1px 5px #800080;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Paranormal Detection Logic ---
def get_paranormal_diagnosis(user_input):
    prompt = f"""
    You are a seasoned paranormal investigator. Analyze the following report and detect possible anomalies:

    Report: "{user_input}"

    Use mystical and analytical language. Mention residual energies, spectral echoes, known haunting types, or energy signatures. Keep the tone spooky but serious.
    """
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"👻 Could not complete analysis: {e}")
        return ""

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🔍 Paranormal Detector", "📁 Case Files", "💡 Paranormal Insights"])

# === TAB 1: DETECTOR ===
with tab1:
    st.header("🔍 Paranormal Activity Detector")
    st.write("Describe any strange occurrences. Our spectral system will analyze it.")

    user_input = st.text_area("📝 Enter your experience:", height=160, placeholder="E.g., Cold spots in the hallway, whispers at night...")

    if st.button("Analyze Report"):
        if user_input.strip():
            with st.spinner("📡 Scanning dimensional disturbances..."):
                result = get_paranormal_diagnosis(user_input)
            st.subheader("📋 Analysis Result:")
            st.success(result)
        else:
            st.warning("☠️ Please describe the anomaly first.")

# === TAB 2: CASE FILES ===
with tab2:
    st.header("📁 Archived Paranormal Case Files")

    case_files = [
        ("🪞 The Mirror That Wept", "In Shimla, a mirror fogged mysteriously each night. EVP sessions captured a whisper: 'Still watching'. The mirror was removed. The activity ceased."),
        ("🕰️ The Time Loop Attic", "Every night at 2:17 AM, footsteps echoed in an attic. A clock was stuck, and shadow figures repeated nightly. Time loop confirmed."),
        ("🌫️ The Fog Walker", "In Himachal, a foggy silhouette appeared and vanished mid-stride. Temperature drops and EMF spikes were detected along its path."),
        ("💡 Lightless Corridor", "A Kolkata office reported lights that never turned on after midnight. Thermal imaging showed a figure standing still for hours."),
        ("🎶 The Singing Room", "In a farmhouse, faint lullabies were heard nightly. An old gramophone, unplugged for years, was found spinning."),
        ("📸 Ghost in the Frame", "At a wedding, a photo revealed a woman no one recognized. Forensic tests confirmed no editing. Locals say it's the bride’s great-grandmother."),
        ("🔒 The Locked Room", "A sealed room in an abandoned hospital had scratching sounds. When broken open, it was empty, but claw marks lined the inside walls."),
    ]

    for title, content in case_files:
        st.subheader(title)
        st.markdown(content)
        st.markdown("---")

# === TAB 3: INSIGHTS ===
with tab3:
    st.header("💡 Paranormal Insights from the Other Side")

    insights = [
        "🔮 *A sudden chill isn't the wind. It's a presence seeking to be felt.*",
        "📻 *Static at midnight often carries whispers from the forgotten.*",
        "🕯️ *If a candle flickers without breeze, someone unseen watches you.*",
        "🧲 *Strong EMF spikes around you may indicate a spectral convergence.*",
        "💤 *Dreams of departed loved ones often mark visitations, not memories.*",
        "🧊 *Ice-cold air near the neck? Spirits prefer the spine.*",
        "⏳ *Repeating the same event nightly? You’re caught in a time echo.*",
        "🎭 *Mimicry of voices from empty rooms is never friendly.*",
        "📿 *Protective items warm in danger. If they go cold, beware.*",
        "🕰️ *3:00 AM is not the witching hour. It’s the observing hour.*",
    ]

    for tip in insights:
        st.markdown(f"- {tip}")
