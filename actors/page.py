import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

ACTORS_LIST = [
    {
        'id': 1,
        'name': 'Andrew'
    },
    {
        'id': 2,
        'name': 'Pedro'
    },
    {
        'id': 3,
        'name': 'Paulo'
    },
]


def show_actors():
    st.write('Lista de atores: ')
    df_actors = pd.DataFrame(ACTORS_LIST)
    AgGrid(
        data=df_actors,
        fit_columns_on_grid_load=True,
        key='actors_grid',
    )

    st.title('Cadastrar Ator: ')
    name = st.text_input('Nome: ')
    if st.button('Cadastrar'):
        st.success(f'Ator "{name}" cadastrado com sucesso!')
