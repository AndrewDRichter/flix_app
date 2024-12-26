import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from utils.decorators import login_decorator
from movies.service import MovieService
from datetime import datetime
from genres.service import GenreService
from actors.service import ActorService


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
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes: ')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            fit_columns_on_grid_load=True,
            key='movies_grid',
        )
    else:
        st.error('Nenhum filme encontrado.')

    st.title('Cadastrar Filme: ')
    title = st.text_input('Título: ')
    release_date = st.date_input(
         label='Data de lançamento',
         value=datetime.today(),
         min_value=datetime(1800, 1, 1).date(),
         max_value=datetime.today(),
         format='DD/MM/YYYY',
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
         label='Gênero',
         options=list(genre_names.keys()),
    )
    genre = genre_names[selected_genre_name]

    actor_service = ActorService()
    actor_choices = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actor_choices}
    selected_actors_names = st.multiselect(
         label='Atores',
         options=list(actor_names.keys()),
    )
    actors = [actor_names[actor] for actor in selected_actors_names]

    summary = st.text_area(
         label='Resumo'
    )
    if st.button('Cadastrar'):
        new_movie = movie_service.create_movies(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            summary=summary,
        )
        if new_movie:
            st.rerun()
            st.success(f'Filme "{title}" cadastrado com sucesso!')
        else:
            st.error('Erro ao cadastrar filme.')
