import streamlit as st
st.header("BODY MASS INDEX")
weight=st.number_input("Enter your weight in kgs")
status=st.radio("Select your height in",("Feet","Centimeters","Meters"))
if status=="Feet":
    height=st.number_input("Enter the height in Feets:")
    if height >0 :
        BMI=weight/ (height / 3)**2
        
    else:
        st.write("Invalid")
elif status=="Centimeters":
    height1=st.number_input("Enter the height in centimeters:")
    if height1>0:
        BMI=weight/(height1/100)**2
        
    else:
        st.write("Invalid")
elif status=="Meters":
    height2=st.number_input("Enter the height in meters:")
    if height2>0:
        BMI=weight/(height2)**2
        
    else:
        st.write("Invalid")
if st.button("CALCULATE BMI"):
    st.write("YOUR BODY MASS INDEX:",BMI)
    if (BMI<16):
        st.error("You are extremely underweight")
    elif(BMI>=16 and BMI<18.5):
        st.warning("You are underweight")
    elif(BMI>=18.5 and BMI<25):
        st.success("YOU ARE HEALTHY")
        st.balloons()
    elif (BMI>=25 and BMI<30):
        st.warning("You are overweight")
    elif(BMI>=30):
        st.error("You are extremely overweight")
