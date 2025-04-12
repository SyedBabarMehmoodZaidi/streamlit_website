import streamlit as st

st.set_page_config(
    page_title="Welcome To My Streamlit App",
    page_icon=":tada:",
    layout="wide",)

#Header Section 

with st.container():

  st.subheader("Hi i am Bamsi :wave:")
  st.title("I am a web developer")
  st.write("I am a web developer who loves to create web applications using streamlit and python and i am also a youtuber :point_left:")
  st.write("[Leaer more >](www.youtube.com/@BabarBamsi90)")

#what i do section

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do 💻✨")
        st.write("##")
        st.write("Crafting digital experiences with code and creativity!")
        st.write(
             """
    I am a passionate and goal-oriented web developer who loves transforming ideas into powerful, user-friendly web applications using **Streamlit** and **Python**.

    Here's what I do:

    - 🚀 **Web Application Development**  
      I design and develop modern, interactive, and responsive web applications using Streamlit and Python. My focus is on building apps that are clean, efficient, and easy to use.

    - 🎨 **User Interface & Experience (UI/UX)**  
      I pay attention to both functionality and aesthetics — ensuring that every application not only works flawlessly but also looks great and feels intuitive.

    - 📹 **YouTube Content Creation**  
      I run a YouTube channel where I create tutorials, share tips, and explain concepts in a beginner-friendly way. My content helps others learn how to code and build projects of their own.

    - 🧠 **Tech Enthusiast & Lifelong Learner**  
      I constantly explore new tools, frameworks, and trends in web development to keep my skills up-to-date and bring innovative ideas to life.

    Whether it’s coding a new app or creating a helpful video, my mission is to inspire, educate, and contribute to the tech community.
    """
        )


#Interaction section


with st.container():
    st.write("---")
    st.write("##")
    st.markdown("## Click, Smile & Support :heart:")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("https://img.icons8.com/ios-filled/50/000000/facebook-new.png")
        st.button("Like")

    with col2:  
        st.image("https://img.icons8.com/ios-filled/50/000000/twitter.png")
        st.button("Follow")
        

    with col3:
        st.image("https://img.icons8.com/ios-filled/50/000000/instagram-new.png")
        st.button("Share")
        
    
    with col4:
        st.image("https://img.icons8.com/ios-filled/50/000000/youtube-play.png")
        st.button("Subscribe")
        st.balloons()
        st.success("Subscribed Successfully!")



















