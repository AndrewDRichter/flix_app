import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from utils.decorators import login_decorator


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione um opção',
        ['Inicio', 'Gêneros', 'Atores', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Inicio':
        st.write(f'Tela de {menu_option}')

    if menu_option == 'Gêneros':
        show_genres()

    if menu_option == 'Atores':
        show_actors()

    if menu_option == 'Filmes':
        show_movies()

    if menu_option == 'Avaliações':
        show_reviews()


if __name__ == '__main__':
    main()
