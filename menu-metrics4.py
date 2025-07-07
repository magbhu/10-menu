import streamlit as st
import json

# Load multilingual menu JSON
with open("menu_data.json", "r", encoding="utf-8") as f:
    MENU = json.load(f)

# --- Language Selector ---
language_labels = {
    "en": "English",
    "ta": "தமிழ்",
    "hi": "हिन्दी",
    "ja": "日本語"
}

st.sidebar.title("🌐 Language")
language = st.sidebar.selectbox(
    "Choose interface language",
    options=list(language_labels.keys()),
    format_func=lambda lang: language_labels[lang]
)

# --- App Header ---
st.markdown(
    f"<h2 style='margin-bottom:0.2em'>{MENU['menu_title'][language]}</h2>",
    unsafe_allow_html=True
)
st.caption(MENU['menu_description'][language])
st.markdown(f"<div style='margin-bottom:1.2em'><strong>🧭 Benefits:</strong><br>{MENU['benefits'][language]}</div>", unsafe_allow_html=True)

# --- Menu Items by Category ---
for category in MENU["menu_categories"]:
    cat_label = category["category"][language]
    with st.expander(f"📂 {cat_label}", expanded=True):
        for item in category["items"]:
            icon = item["icon"]
            label = item["menu_name"][language]
            url = item["url"]

            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 12px; margin-bottom: 10px; background: #f9f9f9;">
                    <a href="{url}" target="_blank" style="text-decoration: none; color: inherit;">
                        <div style="font-size: 1.05em;"><strong>{icon} {label}</strong></div>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
