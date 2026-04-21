import streamlit as st
import requests

API_URL = "http://localhost:8080"
st.title("RAG App")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file and st.button("Upload & Index"):
    files = {
        "file": (uploaded_file.name, uploaded_file, "application/pdf")
    }

    res = requests.post(f"{API_URL}/upload", files=files)
    st.write(res.json())

query = st.text_input("Ask something about the document")

if query:
    res = requests.post(
        f"{API_URL}/query",
        json={"query": query}
    )

    if res.status_code == 200:
        data = res.json()
        st.write("### Answer")
        st.write(data["answer"])

        st.write("### Sources")
        for s in data["sources"]:
            st.write(s)