import streamlit as st
from rapidfuzz import fuzz
import uuid
import time

# --- Setup ---
st.set_page_config(page_title="Velvet", layout="centered")
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())
if "mode" not in st.session_state:
    st.session_state["mode"] = "Solo"
if "mood" not in st.session_state:
    st.session_state["mood"] = "Velvet"

# --- Sidebar Navigation ---
st.sidebar.title("🧭 Velvet Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Mood", "Fantasy Vault", "Sensory Timer", "Reflection"])

# --- Welcome Page ---
if page == "Welcome":
    st.title("💘 Welcome to Velvet")
    st.markdown("Your private space for romantic exploration and emotional connection.")
    mode = st.radio("Choose your mode:", ["Solo", "Couple"])
    st.session_state["mode"] = mode
    st.success(f"Mode set to: {mode}")

# --- Mood Selector ---
elif page == "Mood":
    st.title("🎨 Select Your Mood")
    mood = st.selectbox("Pick a vibe:", ["Velvet", "Rainy", "Playful", "Slow Burn"])
    st.session_state["mood"] = mood
    st.success(f"Mood set to: {mood}")

# --- Fantasy Vault (Couple Only) ---
elif page == "Fantasy Vault":
    if st.session_state["mode"] == "Couple":
        st.title("🔐 Fantasy Vault")
        hide_input = st.checkbox("Hide fantasies while typing?", value=False)

        if hide_input:
            fantasy_a = st.text_input("Partner A fantasy", type="password")
            fantasy_b = st.text_input("Partner B fantasy", type="password")
        else:
            fantasy_a = st.text_area("Partner A fantasy")
            fantasy_b = st.text_area("Partner B fantasy")

        def match_fantasies(f1, f2):
            score = fuzz.token_sort_ratio(f1.lower(), f2.lower())
            return score

        if st.button("Match Fantasies"):
            if fantasy_a and fantasy_b:
                score = match_fantasies(fantasy_a, fantasy_b)
                st.markdown(f"### 🔍 Match Score: `{score}%`")
                if score > 80:
                    st.success("✨ It's a match! You both desire the same thing.")
                elif score > 50:
                    st.info("💡 Close match. Maybe explore this together?")
                else:
                    st.warning("🕊️ No match. Try syncing your desires more openly.")
            else:
                st.error("Please enter fantasies for both partners.")
    else:
        st.warning("Fantasy Vault is only available in Couple mode.")

# --- Sensory Timer ---
elif page == "Sensory Timer":
    st.title("🕯️ Sensory Timer")
    st.markdown("Focus on breath, sound, and touch...")
    duration = st.slider("Duration (minutes)", 1, 10, 3)

    if st.button("Start Sensory Journey"):
        for i in range(duration * 60):
            st.write(f"Time left: {duration*60 - i} seconds")
            time.sleep(1)
        st.success("Session complete. Ready to reflect?")

# --- Reflection Journal ---
elif page == "Reflection":
    st.title("📓 Reflection Journal")
    st.markdown(f"Your selected mood: **{st.session_state['mood']}**")
    notes = st.text_area("How did you feel?")
    rating = st.slider("Rate the experience", 1, 10)

    if st.button("Save Reflection"):
        st.success("Reflection saved. Thank you for sharing.")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ for intimacy, privacy, and emotional connection.")
