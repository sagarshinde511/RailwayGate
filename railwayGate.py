import streamlit as st
import requests

# Dummy credentials
USERNAME = "admin"
PASSWORD = "password"

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def main_app():
    st.title("Control Panel")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    toggle = st.checkbox("Switch", key="switch_state")

    # Determine f1 value
    f1_value = 1 if toggle else 0
    api_url = f"https://aeprojecthub.in/flagChange.php?f5=1&f1={f1_value}"

    if st.button("Send API Request"):
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                st.success(f"API called with f1={f1_value}")
            else:
                st.error(f"Failed to call API. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")

    # Show Gate Status Circle
    status_text = "Gate ON" if toggle else "Gate OFF"
    circle_color = "red" if toggle else "green"

    st.markdown(
        f"""
        <div style='display: flex; align-items: center; gap: 20px; margin-top: 20px;'>
            <div style='
                width: 100px;
                height: 100px;
                border-radius: 50%;
                background-color: {circle_color};
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 18px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            '>{status_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Run the app
if st.session_state.logged_in:
    main_app()
else:
    login()
