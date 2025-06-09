import streamlit as st
from login.page import show_login


def login_decorator(func):
    '''
        Login decorator for functions that should not be viewed by unauthenticated users.

        Usage: Simply put @login_decorator above your function and everything should work fine.

        Example:

        @login_decorator
        def my_page_function():
            st.title('My page')
            st.button('My button')
    '''
    def wrapper():
        '''
        Your api should return a token string containing your authentication token.

        If you are already logged in, the token contained in st.session_state
        will bypass the if statement and call the function wrapped by this decorator.
        '''
        if 'token' not in st.session_state:
            show_login()
        else:
            func()
        return func

    return wrapper
