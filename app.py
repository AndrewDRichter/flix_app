import streamlit as st
from genres.page import show_genres


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
        st.write(f'Tela de {menu_option}')

    if menu_option == 'Filmes':
        st.write(f'Tela de {menu_option}')

    if menu_option == 'Avaliações':
        st.write(f'Tela de {menu_option}')


if __name__ == '__main__':
    main()
