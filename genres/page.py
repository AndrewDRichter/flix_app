import streamlit as st


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

def show_genres():
    st.write('Lista de Gêneros: ')
    st.table(GENRES_LIST)

    st.title('Cadastrar Gênero: ')
    name = st.text_input('Nome: ')
    if st.button('Cadastrar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')
