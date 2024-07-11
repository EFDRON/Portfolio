import streamlit as st
import pandas as pd
import google.generativeai as genai
import time
from streamlit_option_menu import option_menu
import os

api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


def text_generator(text):
    # response = "Sanadek is a user-friendly geospatial data platform designed to make complex data accessible and actionable. Through interactive maps, charts, and graphs, users can explore datasets with ease, uncovering trends and patterns that drive informed decision-making."
    for word in text.split():
        yield word + " "
        time.sleep(0.05)



def main():
    global response
    i = 0
    st.set_page_config(
        page_title="Personal Portfolio",
        page_icon="data/logo.png",
        layout="wide",
        initial_sidebar_state="expanded")
    c1,c2,c3=st.columns([1,3,1])
    #c2.image("images/cv.jpeg")

    if "status" not in st.session_state:
        st.session_state.status="Home"

    selected = option_menu(menu_title="menu,
                           options=["Ask AI", "Projects", "Home","VR Mode"],
                           icons=["house", "book", "robot","headset-vr"],
                           orientation="horizontal"
                           )
    if selected=="Ask AI":
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(" ")
            st.subheader(" ")
            st.subheader("Hi :wave:")
            st.title("I am Murtaza Hassan ")
        
        with col2:
            st.image("images/cv.jpeg")
        
        st.write("")  # Add a single line of space
        st.write("")  # Add a single line of space

         persona = """ You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza) Answer as if you are responding . dont answer in second or third person.
            If you don't know they answer you simply say "That's a secret". Here is more info about Murtaza:
            He is currently studying electrical engineering at higher college of technology Sharjah, UAE. he has good communication,leadership and project management skills which are demonestrated on various projects both
            in curricular and extracurricular projects and acivities.
            """

        if "messages" not in st.session_state:
            st.session_state.messages = []
            # st.session_state.chat_engine = chat_engine
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
            # st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("please enter your prompt"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            response=model.generate_content(persona+'Here is the question:'+prompt)
            with st.chat_message("assistant"):
                # response = prompt_engine.chat(prompt)
                st.write_stream(text_generator(response.text))
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    
        
        
    elif selected=="Datas":
        pass
        

    elif selected=="Home":
       


if __name__ == '__main__':
    main()


