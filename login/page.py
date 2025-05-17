import streamlit as st
from login.service import login


def show_login():
    st.title('Login')
    username = st.text_input('Digite seu username')
    password = st.text_input(
        label='Password',
        type='password',
    )

    if st.button('Fazer login'):
        login(username=username, password=password)
