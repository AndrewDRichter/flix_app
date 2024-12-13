import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


REVIEWS_LIST = [
    {
        'id': 1,
        'user': 1,
        'movie': 1,
        'stars': 3.5,
        'comment': 'Not a bad movie!'
    },
    {
        'id': 2,
        'user': 1,
        'movie': 2,
        'stars': 2,
        'comment': 'Not a good movie!'
    },
    {
        'id': 3,
        'user': 2,
        'movie': 1,
        'stars': 5,
        'comment': 'Great movie!'
    },
]


def show_reviews():
    st.write('Lista de Avaliações: ')
    df_reviews = pd.DataFrame(REVIEWS_LIST)
    AgGrid(
        data=df_reviews,
        fit_columns_on_grid_load=True,
        reload_data=True,
        key='reviews_grid',
    )

    st.title('Cadastrar Avaliação: ')
    comment = st.text_input('Comentário: ')
    if st.button('Cadastrar'):
        st.success(f'Avaliação "{comment}" cadastrado com sucesso!')
