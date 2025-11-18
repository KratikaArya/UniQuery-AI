import streamlit as st
from utils.data_handle import load_data, answer_query

st.set_page_config(page_title="UniQueryAI", page_icon="🎓")
st.title("🎓 UniQueryAI — Your College Info Assistant")
st.caption("Ask me about fees, hostels, libraries, labs, and more!")

@st.cache_data
def get_data():
    return load_data("data/colleges.xlsx")

df = get_data()

domain_options = df["domain_normalized"].unique()
selected_domain = st.selectbox("Choose a domain:", options=domain_options)

df = df[df["domain_normalized"] == selected_domain]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there 👋! I’m UniQueryAI. Ask me about any college’s fees, facilities, or available branches."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_query := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)
    with st.chat_message("assistant"):
        response = answer_query(df, user_query)
        if isinstance(response, str):
            st.markdown(response)
        else:
            st.dataframe(response)  # if it’s a DataFrame (list of colleges)
        st.session_state.messages.append({"role": "assistant", "content": str(response)})
