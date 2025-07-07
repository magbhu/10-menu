import streamlit as st
import json

# Load your full JSON config
with open("menu_data.json", "r", encoding="utf-8") as f:
    MENU = json.load(f)

# Sidebar: Language selector
st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox(
    "Choose interface language", 
    options=["en", "ta", "hi", "ja"],
    format_func=lambda lang: {
        "en": "English",
        "ta": "தமிழ்",
        "hi": "हिन्दी",
        "ja": "日本語"
    }[lang]
)

# Header section
st.title(MENU["menu_title"][language])
st.caption(MENU["menu_description"][language])
st.markdown(f"**🧭 Benefits:**\n{MENU['benefits'][language]}")

st.divider()

# Render each category
for category in MENU["menu_categories"]:
    with st.expander(f"📂 {category['category'][language]}", expanded=True):
        for item in category["items"]:
            icon = item["icon"]
            label = item["menu_name"][language]
            url = item["url"]
            st.markdown(
                f"{icon} [**{label}**]({url})",
                unsafe_allow_html=True
            )
