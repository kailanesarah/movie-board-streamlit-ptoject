from home.repository import MoviesStatesRepository
import streamlit as st


class MoviesStatesService():
    def __init__(self):
        self.movies_states_repository = MoviesStatesRepository()

    def get_movies_states(self):
        if 'movies_states' in st.session_state:
            return st.session_state.movie_states

        movies_states = self.movies_states_repository.get_movies_states()
        st.session_state.movies_states = movies_states
        return movies_states
