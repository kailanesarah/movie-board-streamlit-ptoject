import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from movies.service import MoviesService
from genres.service import GenreService
from actors.service import ActorsService


def show_movies():
    '''LIST MOVIES'''
    st.title('🎬 Movie List')

    movies_service = MoviesService()
    movies = movies_service.get_movie()

    if movies:
        try:
            for movie in movies:
                movie['actors'] = ', '.join(actor['name'] for actor in movie['actors'])
            movies_df = pd.json_normalize(movies)
            AgGrid(
                data=movies_df,
                reload_data=True,
                key='movies_grid'
            )
        except Exception as e:
            st.error(f"Error while processing movie data: {str(e)}")
    else:
        st.warning('⚠️ Unable to load the movie list.')

    '''REGISTER NEW MOVIE'''
    st.header('📥 Register a New Movie')

    name = st.text_input(label='Movie Title', placeholder='Enter the movie title')

    release_date = st.date_input(
        label='Release Date',
        format='DD/MM/YYYY'
    )

    genres_service = GenreService()
    genres_list = genres_service.getGenre()
    genres_name = {genre['name']: genre['id'] for genre in genres_list}
    selected_genre_name = st.selectbox('Genre', list(genres_name.keys()))

    actors_service = ActorsService()
    actors_list = actors_service.get_actors()
    actors_name = {actor['name']: actor['id'] for actor in actors_list}
    selected_actors = st.multiselect('Actors/Actresses', list(actors_name.keys()))

    resume = st.text_area('Movie Summary')

    if st.button('Register Movie'):
        if name and selected_genre_name and selected_actors and resume:
            data_movie = {
                'name': name,
                'release_date': release_date.strftime('%Y-%m-%d'),
                'genres': selected_genre_name,
                'actors': selected_actors,
                'resume': resume,
            }
            movies_service.post_movies(data_movie)
            st.success(f'✅ The movie "{name}" was successfully registered!')
        else:
            st.warning("⚠️ Please fill in all fields before registering.")
