import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":globe_showing_asia_australia:", layout="wide")


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

        
        
