

import streamlit as st
from image_bg_foodify import front_page
from login_foodify import log_in_foodify
from signup_foodify import sign_up_foodify
from menu_display import display_menu_multiselect
from cart import display_cart
from billing_foodify import billing_food
from payment import payment_foodify

st.logo("ride_foodify_img.png",size="large")


# Initialize session state variables
if "page" not in st.session_state:
    st.session_state["page"] = "front"
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

def main_foodify():
    if st.session_state["logged_in"]:
        st.sidebar.write(f"Logged in as: {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["page"] = "front"
            st.rerun()
        if st.session_state["page"] == "menu":
            display_menu_multiselect()
        elif st.session_state["page"] == "cart":
            display_cart()
        elif st.session_state["page"]=="billing":
            billing_food()
        elif st.session_state["page"]=="pay":
            payment_foodify()
        else:
            # Default to menu if an unknown page
            st.session_state["page"] = "menu"
            st.rerun()
    else:
        if st.session_state["page"] == "front":
            front_page()
        elif st.session_state["page"] == "login":
            log_in_foodify()
        elif st.session_state["page"] == "signup":
            sign_up_foodify()
        

if __name__ == "__main__":
    main_foodify()








