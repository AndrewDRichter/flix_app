import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from utils.decorators import login_decorator


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


@login_decorator
def show_genres():
    st.write('Lista de Gêneros: ')
    df_genres = pd.DataFrame(GENRES_LIST)
    AgGrid(
        data=df_genres,
        fit_columns_on_grid_load=True,
        reload_data=True,
        key='genres_grid',
    )

    st.title('Cadastrar Gênero: ')
    name = st.text_input('Nome: ')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
