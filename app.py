import streamlit as st

st.set_page_config(page_title="UniQueryAI", page_icon="🎓", layout="centered")

st.title("🎓 Welcome to UniQueryAI")
st.markdown(
    """
    ### Your Personal College Info Assistant  
    Get instant answers about college **fees**, **facilities**, **hostels**, **labs**, and more.  
    Explore colleges by domain and ask questions naturally — powered by smart data handling!
    """
)

st.image("https://cdn-icons-png.flaticon.com/512/1048/1048943.png", width=180)

st.markdown("---")
st.subheader("🚀 Ready to get started?")

if st.button("Go to Chatbot 💬"):
    st.switch_page("pages/1_Chatbot.py")
