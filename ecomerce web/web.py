import streamlit as st
import random

# Set background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://source.unsplash.com/1600x900/?shopping,ecommerce');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample product catalog with categories
categories = {
    "Electronics": {
        "Laptop": {"price": 800, "image": "💻"},
        "Smartphone": {"price": 500, "image": "📱"},
        "Tablet": {"price": 300, "image": "📟"},
    },
    "Accessories": {
        "Headphones": {"price": 100, "image": "🎧"},
        "Smartwatch": {"price": 150, "image": "⌚"},
        "Camera": {"price": 600, "image": "📷"},
    }
}

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Header
st.markdown("""
    <h1 style='text-align: center; color: white;'>🛒 Welcome to eCommerce Store</h1>
    <hr>
""", unsafe_allow_html=True)

# Navigation
menu = ["Home", "Cart", "Checkout", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Categories")
    for category, products in categories.items():
        st.markdown(f"### {category}")
        for product, details in products.items():
            col1, col2, col3 = st.columns([1, 3, 1])
            col1.write(details["image"])
            col2.write(f"**{product}** - ${details['price']}")
            if col3.button(f"Add {product}"):
                if product in st.session_state.cart:
                    st.session_state.cart[product] += 1
                else:
                    st.session_state.cart[product] = 1
    
elif choice == "Cart":
    st.subheader("🛍️ Your Cart")
    if st.session_state.cart:
        total_price = 0
        for item, quantity in st.session_state.cart.items():
            for category in categories.values():
                if item in category:
                    st.write(f"{item} x {quantity} - ${category[item]['price'] * quantity}")
                    total_price += category[item]['price'] * quantity
        
        st.write(f"**Total: ${total_price}**")
        if st.button("Proceed to Checkout"):
            st.session_state.page = "Checkout"
            st.experimental_rerun()
    else:
        st.write("Your cart is empty.")

elif choice == "Checkout":
    st.subheader("💳 Checkout")
    if st.session_state.cart:
        st.write("Enter your details for payment:")
        name = st.text_input("Full Name")
        address = st.text_area("Shipping Address")
        card_number = st.text_input("Card Number", type="password")
        if st.button("Confirm Purchase"):
            order_id = random.randint(1000, 9999)
            st.success(f"Thank you for your purchase! 🎉 Your order ID is {order_id}.")
            st.session_state.cart = {}
    else:
        st.write("Your cart is empty.")

elif choice == "Contact":
    st.subheader("📞 Contact Us")
    st.write("For inquiries, email us at support@estore.com or call +1234567890.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: white;'>© 2025 eCommerce Store. All rights reserved.</p>
""", unsafe_allow_html=True)
