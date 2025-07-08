import streamlit as st
import json
import os
import datetime

user_file = "foodify_users.json"

def load_users():
    if not os.path.exists(user_file):
        return {}
    with open(user_file, "r") as f:
        return json.load(f)

def save_users(users):
    with open(user_file, "w") as f:
        json.dump(users, f, indent=4)

def sign_up_foodify():
    st.title("SIGN UP")
    username = st.text_input("Enter Name",placeholder="Username>=3 Characters")
    if len(username)>=3:
        st.success("Correct username!")
    else:
        st.error("Fill correct username")
    dob = st.date_input("Date of Birth", datetime.date(2000, 1, 1))
    password = st.text_input("Enter Password", type="password")
    def valid_password(pwd):
        is_upper=(c.isupper() for c in pwd)
        is_digit=(c.isdigit() for c in pwd)
        return is_upper and is_digit
    if password:
        if valid_password(password):
            pass
        else:
            st.error("Add a capital letter and a digit to password")
    address = st.text_input("Enter your permanent address")
    email = st.text_input("Enter Email", placeholder="example@gmail.com")
    if "@gmail.com" in email:
        st.success("Valid Email Entered")
    else:
        st.error("Fill Correct Email")
    if st.button("ACCOUNT CONFIRM!",type="primary"):
        if not username or not dob or not password or not address or not email:
            st.error("ERROR: Please fill in all fields.")
            return

        users = load_users()
        if username in users:
            st.error("This username already exists.")
            return

        users[username] = {
            "password": password,
            "dob": str(dob),
            "address": address,
            "email": email
        }
        save_users(users)
        st.success("Great! You have successfully signed up.")
        st.session_state["page"] = "login"
        st.rerun()
    if st.button("Back to Home",type="primary"):
        st.session_state["page"] = "front"
        st.rerun()

