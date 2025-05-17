from movies.repository import MoviesRepository
import streamlit as st


class MoviesService():
    def __init__(self):
        self.movies_repository = MoviesRepository()

    def get_movie(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movies_repository.get_movie()
        st.session_state.movies = movies
        return movies

    def post_movie(self, data_movie):

        movie = dict(
            name=data_movie.get("name"),
            release_date=data_movie.get("release_date"),
            genre=data_movie.get("genre"),
            actors=data_movie.get("actors"),
            resume=data_movie.get("resume"),

        )

        new_movie = self.movies_repository.post_movie(movie)
        st.session_state.movies.append(new_movie)
