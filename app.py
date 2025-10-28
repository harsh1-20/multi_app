import os
os.system("pip install icalendar")
import streamlit as st
from pass_strength import *
from calender import show_calendar
from weather import show_weather
from news import get_news_rss

st.set_page_config(page_title="Multi-Utility App", layout="centered")
st.title("🌐 Multi-Utility App")
st.write("Welcome to the Multi-Utility App! Choose a tool from the sidebar to get started.")
st.sidebar.title("Select a Tool")
page= st.sidebar.radio("select a Feauture",["Password Strength Checker","Indian Holiday Calendar","Weather Info","News Headlines"])

if page=="Home":
    st.title("🌐 Multi-Utility App")
    st.write("""Welcome to the Multi-Utility App! Choose a tool from the sidebar to get started.""")

elif page=="Password Strength Checker":
    check_pwd()
elif page=="Indian Holiday Calendar":
    show_calendar()
elif page=="Weather Info":
    show_weather()
elif page=="News Headlines":
    get_news_rss()

if __name__=='main':
    st.run()
