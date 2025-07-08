import streamlit as st
import json
import os

users_file="users.json"
def load_users():
    if not os.path.exists(users_file):
        return{}
    with open (users_file,"r") as f:
        return json.load(f)
    
def log_in():
    st.title("LOGIN")

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    if st.button("Login"):
        users=load_users()
        if username in users and users[username]==password:
            st.success("LOGIN IS SUCCESFULL!")
            st.session_state["logged in"]=True
            st.session_state["username"]=username
        else:
            st.error("Invalid username and password")
        