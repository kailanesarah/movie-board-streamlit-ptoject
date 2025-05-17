import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from home.service import MoviesStatesService
import plotly.express as px


def show_home():
    st.title('🎬 Movie state')

    movies_state_service = MoviesStatesService()
    movies_state = movies_state_service.get_movies_states()

    if len(movies_state['movies_by_genres']) == 0:
        st.error("We haven't any state")

    try:
        fig = px.pie(
            movies_state['movies_by_genres'],
            values='count',
            names='genre__name',
            title='Filme por gênero'
        )

        st.plotly_chart(fig)

        st.header('Total de filmes cadastrados')
        st.write(movies_state['total_movies'])

        st.header('Total de avaliações cadastradas')
        st.write(movies_state['total_reviews'])

        st.header('Media de avaliação')
        st.write(movies_state['average_stars'])

    except Exception as e:
        st.error(f"Error while processing states data: {str(e)}")
