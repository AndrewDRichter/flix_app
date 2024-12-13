import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from utils.decorators import login_decorator


MOVIES_LIST = [
    {
        'id': 1,
        'name': 'A Felicidade não se compra',
        'duration': '2h23m'
    },
    {
        'id': 2,
        'name': 'Titanic',
        'duration': '1h59m'
    },
    {
        'id': 3,
        'name': 'Esqueceram de mim',
        'duration': '3h02m'
    },
]


@login_decorator
def show_movies():
    st.write('Lista de Filmes: ')
    df_movies = pd.DataFrame(MOVIES_LIST)
    AgGrid(
        data=df_movies,
        fit_columns_on_grid_load=True,
        reload_data=True,
        key='movies_grid',
    )

    st.title('Cadastrar Filme: ')
    name = st.text_input('Nome: ')
    if st.button('Cadastrar'):
        st.success(f'Filme "{name}" cadastrado com sucesso!')
