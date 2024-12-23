import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from utils.decorators import login_decorator
from genres.service import GenreService


@login_decorator
def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros: ')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            fit_columns_on_grid_load=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar Gênero: ')
    name = st.text_input('Nome: ')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genres(
            name=name,
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar gênero.')
