import streamlit as st
import json

# Load multilingual menu JSON
with open("menu_data.json", "r", encoding="utf-8") as f:
    MENU = json.load(f)

# Language selector
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

# Header display
st.markdown(
    f"<h2 style='margin-bottom:0.2em'>{MENU['menu_title'][language]}</h2>",
    unsafe_allow_html=True
)
st.caption(MENU['menu_description'][language])
st.markdown(
    f"<div style='margin-bottom:1.2em; font-size:0.95rem; line-height:1.5;'><strong>🧭 Benefits:</strong><br>{MENU['benefits'][language]}</div>",
    unsafe_allow_html=True
)

# Render each category with styled link cards
for category in MENU["menu_categories"]:
    cat_label = category["category"][language]
    with st.expander(f"📂 {cat_label}", expanded=True):
        for item in category["items"]:
            icon = item["icon"]
            label = item["menu_name"][language]
            url = item["url"]

            st.markdown(
                f"""
                <div style="
                    border: 1px solid #d0d0d0;
                    border-radius: 10px;
                    padding: 14px 18px;
                    margin-bottom: 12px;
                    background: #ffffff;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                ">
                    <a href="{url}" target="_blank" style="
                        text-decoration: none;
                        color: #1a1a1a;
                        font-weight: 600;
                        font-size: 1rem;
                        display: block;
                    ">
                        {icon} {label}
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
