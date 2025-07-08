import streamlit as st
import json
import os

users_file="users.json"
def load_users():
    if not os.path.exists(users_file):
        return {}
    with open (users_file,"r") as f:
        return json.load(f)

def save_users(user):
    with open(users_file,"w") as f:
        json.dump(user,f)

def sign_up():
    st.title("SIGN UP HERE")

    username=st.text_input("ENTER USERNAME:")
    password=st.text_input("ENTER PASSOWORD",type="password")
    confirm_password=st.text_input("CONFIRM PASSWORD",type="password")

    if st.button("Account Confirm"):
        if not username or not password or not confirm_password:
            st.error("Check and Fill again!")
            return
        if password != confirm_password:
            st.error("Passwords does not match!")
            return
        users=load_users()
        if username in users:
            st.error("This username already exists.")
            return
        users[username]=password
        save_users(users)
        st.success("Great!You have successfully signed Up.")
