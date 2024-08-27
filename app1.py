import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emoji's here: https://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":globe_showing_asia_australia:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return none
    return r.jason()


#...Load Assets ...
lottie_coding = load_lottieurl("https://lottie.host/edcad0c9-6e21-4e9c-a1e8-82a2efaceefe/BXGDfV5g1u.json")
#lottie_coding = "https://lottie.host/71d41eef-5a9d-41b4-b232-4960abb94a86/Uj3l65BbJf.json"


# .... Header Section .....
with st.container():
    st.subheader(" Hi, I am Naveen :palm_tree:")
    st.title("A Design Consultant from Los Angeles")
    st.write( "I am passionate about finding ways to use Python and VBA to be more efficient and effective in my business settings")
    st.write("[Learn More>](https://pythonandvba.com)")


# ....What I Do ...
with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for peolple who:
            - are looking for a way to leverage the power of Python in their day to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use python and VBA
            - want to learn Data Analysis & Data Science to perform meaningful and impactful Analysis
            - and working with Excel and found themelves thinking, " there has to be a better way"
            
            If this sounds interesting to you, consider scheduling and turning on the notifications so you do not miss any content
            """
        )
        st.write("[My YouTube Channel >](https://youtube.com/c/CodingIsFun)")

with right_column:
    st.lottie(lottie_coding, height=300, key="coding") 
           
        
