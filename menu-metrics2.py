import streamlit as st
import json
import webbrowser

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
            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                st.markdown(item["icon"])
            with col2:
                label = item["menu_name"][language]
                if st.button(label, key=f"menu-{item['sequence']}"):
                    webbrowser.open_new_tab(item["url"])
