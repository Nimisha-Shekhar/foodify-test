import streamlit as st
st.title("YASH TECHNOLOGIES INTERN REGISTRATION")
from PIL import Image
img=Image.open("download.png")
st.image(img,width=200)
st.text_input("ENTER NAME:")
st.text_input("ENTER SURNAME:")
import datetime
st.date_input("ENTER YOUR DATE OF BIRTH",datetime.date(2000,1,1))
username=st.text_input("ENTER USERNAME:")
password=st.text_input("ENTER PASSWORD:",type="password")
if username.isdigit():
    st.error("ERROR -ENTER CORRECT USERNAME")
else:
    st.success("Thanks!Enter Further Information For Our reference")
email = st.text_input("Enter your email address", placeholder="example@email.com")
contact=st.text_input("ENTER CONTACT NUMBER:",placeholder="XXXXXXXXXX")
if len(contact)!=10:
    st.error("YOU HAVE ENTERED AN INVALID CONTACT NUMBER")
else:
    st.success("THE NUMBER IS VALID!")
address=st.text_input("ENTER YOUR VALID ADDRESS:")
status=st.radio("Gender",("Male","Female","Other"))
occupation=st.text_input("Occupation")
field=st.selectbox("FIELD",["TECHNICAL","MANAGEMENT","STAFF","SECURITY"])
if field=="TECHNICAL" or field=="MANAGEMENT":
    cgpa=st.text_input("ENTER YOUR CGPA OR GPA:")
    if cgpa.isnumeric():
        st.success("Thanks! For entering correct GPA")
    else:
        st.error("Sorry!Re-Enter Correct CGPA")






