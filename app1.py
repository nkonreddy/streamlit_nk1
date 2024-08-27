# Build a website in 12 minutes using Python and Streamlit: https://www.youtube.com/watch?v=VqgUkExPvLY
from PIL imort Image
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
#lottie_coding = "https://lottie.host/3a02227c-ba58-4ce6-a87a-6a81acce8828/9k1zbdwoE9.json"
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

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

        
#....Projects....
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write(##)
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside your Streamlit App")
        st.write(
            """
            Learn how to ue Lottie files in Streamlit!
            Animationmake our web app more engaging and fun, and Lottie Files are the easiest way to do 
            In this tutorial, I"will show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtube/TXSOitGoINE)")
