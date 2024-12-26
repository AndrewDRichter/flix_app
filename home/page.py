import streamlit as st
import plotly.express as px
from movies.service import MovieService
from utils.decorators import login_decorator


@login_decorator
def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por gênero')
        fig = px.pie(
            data_frame=movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig)

    st.subheader('Total de filmes cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Quantidade de filmes por gênero:')
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre['genre__name']}: {genre['count']}')

    st.subheader('Total de avaliações cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média de estrelas em avaliações:')
    st.write(movie_stats['average_stars'])
