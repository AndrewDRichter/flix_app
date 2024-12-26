import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
import pandas as pd
from utils.decorators import login_decorator
from actors.service import ActorService


@login_decorator
def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de atores: ')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            fit_columns_on_grid_load=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum ator encontrado.')

    st.title('Cadastrar Ator: ')
    name = st.text_input('Nome: ')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    NATIONALITY_CHOICES = [
        'USA',
        'BR',
        'PY',
        'AR',
    ]
    nationality = st.selectbox(
        label='Nacionalidade',
        options=NATIONALITY_CHOICES,
    )
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actors(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
            st.success(f'Ator "{name}" cadastrado com sucesso!')
        else:
            st.error('Erro ao cadastrar ator.')
