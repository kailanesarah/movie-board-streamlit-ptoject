import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService


def show_genres():
    '''LIST NEW GENRE'''
    genre_service = GenreService()
    genres = genre_service.getGenre()
    st.write('Genre List')

    if genres:
        try:
            genre_df = pd.json_normalize(genres)
            AgGrid(
                data=genre_df,
                reload_data=True,
                key='genres_grid')
        except Exception as e:
            st.error(f"Error while processing genre data: {str(e)}")
    else:
        st.warning('Error: Could not display the genre list.')

    '''REGISTER NEW GENRE'''
    st.title('Register a New Genre')
    genre_name = st.text_input(label='Genre Name', placeholder='Enter the genre name')

    if st.button('Register New Genre'):
        if genre_name:
            genre_service.postGenre(genre_name)
            st.success(f'New genre "{genre_name}" registered successfully!')
        else:
            st.warning("Please enter a genre name before registering.")
