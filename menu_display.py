import streamlit as st
import json
import os
menu_file="menu.json"

def load_menu():
    if not os.path.exists(menu_file):
        return{}
    with open(menu_file,"r") as f:
        return json.load(f)
    

def display_menu_multiselect():
    col1, col2, col3 = st.columns([1, 1, 3]) 
    with col3:
        st.image("serve_menu.jpeg", width=150)
    st.title("FOODIFY MENU - SELECT ITEMS YOU WANT TO ORDER")
    menu = load_menu()
    if not menu:
        return
    
    quantities={}
    for category, items in menu.items():
        st.subheader(category)
        for idx, item in enumerate(items):
                key = f"{category} - {item['Name']}-{idx}"
                qty = st.number_input(f"{item['Name']} (₹{item['Price']})",
                min_value=0, max_value=20, value=0, step=1,
                key=key
            )
                quantities[key] = {
                    "category": category,
                    "name": item['Name'],
                    "price": item['Price'],
                    "quantity": qty
                }

    from PIL import Image
    img=Image.open("ride_foodify_img.png")
    st.image(img,width=100)

    if st.button("GO TO CART",type="primary"):
        st.session_state["quantities"] = quantities
        st.session_state["page"] = "cart"
        st.rerun()

        

    

