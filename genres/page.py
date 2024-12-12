import streamlit as st


GENRES_LIST = [
    {
        'id': 1,
        'name': 'Fantasy'
    },
    {
        'id': 2,
        'name': 'Drama'
    },
    {
        'id': 3,
        'name': 'Action'
    },
]

def show_genres():
    for genre in GENRES_LIST:
        st.write(genre)
        st.divider()