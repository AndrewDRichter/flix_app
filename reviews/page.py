import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService
from utils.decorators import login_decorator
import pandas as pd
from streamlit_star_rating import st_star_rating


@login_decorator
def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações: ')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            fit_columns_on_grid_load=True,
            key='reviews_grid',
        )
    else:
        st.error('Nenhuma avaliação encontrada.')

    st.title('Avaliar filme: ')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_names = {movie['title']: movie['id'] for movie in movies}
    selected_movie = st.selectbox(
        label='Filme',
        options=list(movie_names.keys()),
    )
    movie = movie_names[selected_movie]
    stars = st_star_rating(
        label='Avalie o filme',
        maxValue=5,
        defaultValue=0,
    )
    comment = st.text_area('Comentário: ')
    if st.button('Cadastrar'):
        new_review = review_service.create_reviews(
            movie=movie,
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
            st.success(f'Avaliação registrada com sucesso!')
        else:
            st.error('Erro ao registrar avaliação.')
