import streamlit as st
from genres.repository import GenreRepository


class GenreService():

    def __init__(self):
        self.genre_repository = GenreRepository()

    def getGenre(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genre()
        st.session_state.genres = genres
        return genres

    def postGenre(self, name_genre):
        genre = dict(
            name=name_genre
        )
        new_genre = self.genre_repository.post_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
