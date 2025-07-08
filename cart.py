import streamlit as st
import json
import os 

def display_cart():
    col1, col2, col3 = st.columns([1, 1, 3]) 
    with col3:
        st.image("cart_img.jpeg", width=150)
    
    st.title("CART")
    st.subheader("YOUR SPECIAL ITEMS ARE AS FOLLOWS:")
    quantities=st.session_state.get("quantities",{})
    cart_items=[v for v in quantities.values() if v["quantity"]>0]
    if cart_items:
        st.success("You have selected the following items:")
        total = 0
        for item in cart_items:
            st.write(f"{item['category']} - {item['name']} x {item['quantity']} = ₹{int(item['price']) * int(item['quantity'])}")
            total += int(item['price']) * int(item['quantity'])
        st.write(f"Total items: {sum(item['quantity'] for item in cart_items)}")
        st.write(f"Total price: ₹{total}")
    else:
        st.warning("No items selected. Please select at least one item.")





    if st.button("BACK TO MENU",type="primary"):
        st.session_state["page"] = "menu"
        st.rerun()
    if st.button("FINAL BILLING",type="primary"):
        st.session_state["quantities"] = quantities
        st.session_state["page"] = "billing"
        st.rerun()





