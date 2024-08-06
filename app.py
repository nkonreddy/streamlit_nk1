import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Hi, I'm Rekha working with my Streamlit experts here.:wave:")


#st.title ("I'm working on becoming a Streamlit Evangelist.")


st.markdown("""
<style>
.normal-font {
    font-size:20px !important;
}
.title-font {
    font-size:30px !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown('<p class="title-font">I\'m working on becoming a Streamlit Evangelist.', unsafe_allow_html=True)


st.markdown('<p class="normal-font">We\'re a passionate team wanted to learn and advance in Python to be more effective and efficient.<br> <a href="https://streamlit.io/"> Learn more about Streamlit.', unsafe_allow_html=True)
#st.write("We're a passionate team wanted to learn and advance in Python to be more effective and efficient.")
#st.write("[Learn more >] (https://streamlit.io)")
