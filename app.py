import streamlit as st 
from login import log_in
from signup import sign_up

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
def main():
    st.sidebar.title("Navigation")
    page=st.sidebar.radio("Go to",["Sign In","Log In","QUIZ"])

    if st.session_state.logged_in:
        st.sidebar.write(f"Logged in as: {st.session_state.username}")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
        st.write("You are logged in! This is a protected page.")
    else:
        if page == "Log In":
            log_in()
        elif page=="Sign In":
            sign_up()
        else:
            quiz()
            

if __name__ == "__main__":
    main()