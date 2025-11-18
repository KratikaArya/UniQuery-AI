import streamlit as st
from utils.data_handle import load_data, answer_query

# --- App Setup ---
st.set_page_config(page_title="UniQueryAI", page_icon="🎓")
st.title("🎓 UniQueryAI — Your College Info Assistant")
st.caption("Ask me about fees, hostels, libraries, labs, and more!")

# --- Load data once ---
@st.cache_data
def get_data():
    return load_data("data/colleges.xlsx")

df = get_data()

# --- Domain selection ---
domain_options = df["domain_normalized"].unique()
selected_domain = st.selectbox("Choose a domain:", options=domain_options)

# Filter dataframe based on domain
df = df[df["domain_normalized"] == selected_domain]

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there 👋! I’m UniQueryAI. Ask me about any college’s fees, facilities, or available branches."}
    ]

# --- Display existing chat messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User input box ---
if user_query := st.chat_input("Type your question here..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate bot response
    with st.chat_message("assistant"):
        response = answer_query(df, user_query)
        if isinstance(response, str):
            st.markdown(response)
        else:
            st.dataframe(response)  # if it’s a DataFrame (list of colleges)
        st.session_state.messages.append({"role": "assistant", "content": str(response)})