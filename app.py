import streamlit as st

# Page setup
st.set_page_config(page_title="UniQueryAI", page_icon="🎓", layout="centered")

# --- Landing Page Content ---
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

# --- Redirect Button ---
if st.button("Go to Chatbot 💬"):
    # Streamlit page navigation workaround
    js = "window.location.href = '/1_Chatbot';"
    st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
