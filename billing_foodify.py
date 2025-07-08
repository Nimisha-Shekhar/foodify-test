import streamlit as st
import json
import os

def billing_food():
    col1, col2, col3 = st.columns([1, 1, 3]) 
    with col3:
        st.image("bill_img.jpeg", width=150)
    st.title("FOODIFY TOTAL EXPENSES-CHECK")
    from PIL import Image
    img=Image.open("ride_foodify_img.png")
    st.image(img,width=100)
    
    quantities=st.session_state.get("quantities",{})
    cart_items=[v for v in quantities.values() if v["quantity"]>0]
    if cart_items:
        st.success("You have selected the following items:")
        total_price = 0
        for item in cart_items:
            st.write(f"{item['category']} - {item['name']} x {item['quantity']} = ₹{int(item['price']) * int(item['quantity'])}")
            total_price += int(item['price']) * int(item['quantity'])
        st.write(f"Total items: {sum(item['quantity'] for item in cart_items)}")
        st.write(f"Total price: ₹{total_price}")
        final_price = total_price * 10/100
        tfinal_price= total_price* 9/100
        delivery_charge=100
        super_final= total_price + final_price + tfinal_price + delivery_charge
        st.markdown(f"### The total order price is: ₹{total_price}")
        st.markdown(f"### 10% convinience fee:₹{final_price}")
        st.markdown(f"### 9% GST:₹{tfinal_price}")
        st.markdown(f"### Delivery Charge:₹{delivery_charge}")
        st.warning(f"## FINAL AMOUNT:₹{super_final}")
    else:
        st.warning("No items selected. Please select at least one item.")


    if st.button("BACK TO CART",type="primary"):
        st.session_state["page"] = "cart"
        st.rerun()
    if st.button("PAY HERE",type="primary"):
        st.session_state["page"]="pay"
        st.rerun()

