# --- Fantasy Vault ---
if mode == "Couple":
    st.subheader("🔐 Fantasy Vault")

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
