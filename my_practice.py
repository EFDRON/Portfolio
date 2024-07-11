import streamlit as st
import pandas as pd
import google.generativeai as genai
import time
from streamlit_option_menu import option_menu
import os

#api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key="AIzaSyDXKDsRRF_fMkPZaRgl1Adhe7FoYcf9-tk")

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("who are you")
print(response.text)
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

    selected = option_menu(menu_title=None,
                           options=["Home", "Projects", "Ask AI","VR Mode"],
                           icons=["house", "book", "robot","headset-vr"],
                           orientation="horizontal"
                           )
    if selected=="Home":
        i=0
        t1,t2=st.columns([1,8])
        t1.image("images/cv.jpeg")
        t2.write_stream(text_generator("## Welcome to Sanadek Geospatial Data Platform!"))

        #image=open("C:/Users/efake/Downloads/_65a22b0b-8e1e-46c0-87e9-9878ea7e0080.jpeg")
        st.write("### Unlock the Power of Data Visualization for Community Development")
        col1,col2,col3=st.columns([1,5,1])
        #col2.image("C:/Users/efake/Downloads/_65a22b0b-8e1e-46c0-87e9-9878ea7e0080.jpeg",width=600)

        st.write("**At Sanadek, we believe that data should be more than just numbers on a page. Our platform transforms raw data into dynamic visualizations, empowering users to gain valuable insights and drive positive change in their communities.**")
        st.subheader("What is Sanadek?")
        s1,s2,s3=st.columns((1,5,3))
        #s2.image("C:/Users/efake/Downloads/_453197d0-21b5-4fd7-9319-e2bcd9c793a1.jpeg",width=600)

        with s3:
            ("  "
             ""
             "")
            #st.image("data/images/quotation_marko-removebg-preview.png",width=100)
            st.write_stream(text_generator("Sanadek is a user-friendly geospatial data platform designed to make complex data accessible and actionable. Through interactive maps, charts, and graphs, users can explore datasets with ease, uncovering trends and patterns that drive informed decision-making."))
            st.write_stream(text_generator("In essence, Sanadek is more than just a data platform—it's a gateway to actionable insights and informed decision-making. By democratizing access to geospatial data and empowering users with intuitive tools, Sanadek is driving positive change and transformation in diverse domains, ultimately contributing to a more sustainable and prosperous future."))
            #st.write("Sanadek is a user-friendly geospatial data platform designed to make complex data accessible and actionable. Through interactive maps, charts, and graphs, users can explore datasets with ease, uncovering trends and patterns that drive informed decision-making.")

        st.subheader("How to Use Sanadek:")
        st.write("**1. Explore Data:** Dive into our extensive database of community development data. Search by location, topic, or dataset to find the information you need." )
        st.image("C:/Users/efake/Pictures/Screenshots/Screenshot 2024-04-14 195216.png")
        st.write("**2. Visualize Insights:** Engage with your data like never before. Our intuitive visualization tools bring your data to life, making it easy to spot trends, identify opportunities, and track progress over time.")
        C1,C2,C3=st.columns([1,4,1])
        #with C2:
            #st.image("C:/Users/efake/Downloads/_f002fb34-54cb-42f6-a6cf-d9043c01174f.jpeg",width=400)
        st.write("**3. Interact Dynamically:** Take control of your analysis with interactive features. Zoom in, filter, and customize visualizations to focus on what matters most to you.")
        st.write("**4. Gain Insights with AI:** Ask questions and receive instant insights with our AI-powered analytics. From simple queries to complex analyses, our platform provides the answers you need, when you need them.")
        st.subheader("Ready to Get Started?")
        st.write("Join the Sanadek community today and unlock the full potential of your data for community development. Sign up for a free account or explore our demo to see Sanadek in action.")
        st.subheader("About Us")
        st.text("Developed by Team Sanadek")
        st.text("UAE Hackathon 2024")
        st.session_state.status="Home"
    elif selected=="Datas":
        i=1

        st.session_state.status="Datas"
        datas=["","People of Determination","Public Associations","Marriage Grants","Mass Weddings","Social Security","Relief","Financial Markets","Insurance","Business Registration","Money and Banking","Labor Force","National Accounts","Prices and Indices","Foreign Investment","Financial Market","Custom Duty","Pension","Metal Industries","Tourism","International Trade","Money and Banking","Prices and Indices","Foreign Investement"]
        data_type=st.selectbox("Select Type of Data",datas)
        if data_type=="":
            st.write("Choose data to start")

        else:
            if data_type=="People of Determination":

                st.write_stream(text_generator("### People of Determination Data"))
                st.caption("Source: Ministry Of Community Development")


            elif data_type=="Public Associations":
                st.subheader("Public Associations Data")
                st.caption("Source: Ministry Of Community Development")




    elif selected=="Ask AI":
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


if __name__ == '__main__':
    main()


