

import streamlit as st
import json
import os

user_file = "foodify_users.json"

def load_users():
    if not os.path.exists(user_file):
        return {}
    with open(user_file, "r") as f:
        return json.load(f)

def log_in_foodify():
    st.title("LOGIN")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("LOGIN",type="primary"):
        users = load_users()
        if username in users and users[username]["password"] == password:
            st.success("LOGIN SUCCESSFUL")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["page"] = "menu"
            st.rerun()
        else:
            st.error("ERROR: This account does not exist or password is incorrect!")
    if st.button("Go to Sign Up",type="primary"):
        st.session_state["page"] = "signup"
        st.rerun()
    if st.button("Back to Home",type="primary"):
        st.session_state["page"] = "front"
        st.rerun()
