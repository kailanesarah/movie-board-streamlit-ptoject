import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewsService
from movies.service import MoviesService


def show_reviews():
    '''LIST NEW REVIEWS'''
    reviews_service = ReviewsService()
    reviews = reviews_service.get_reviews()
    st.write('Review list')

    if reviews:
        try:
            reviews_df = pd.json_normalize(reviews)
            AgGrid(
                data=reviews_df,
                reload_data=True,
                key='reviews_grid')
        except Exception as e:
            st.error(f"Error while processing reviews data: {str(e)}")
    else:
        st.warning('Error: Could not display the reviews list.')

    '''REGISTER NEW REVIEWS'''
    st.title('Register a New Reviews')

    movies_service = MoviesService()
    movies = movies_service.get_movie()
    st.write(movies)
    movie_titles = {movie['name']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filmes', movie_titles.keys())

    stars = st.number_input(
        label='Stars',
        min_value=1,
        max_value=5,
        step=1
    )

    comment = st.text_area('Deixe seu comentário')

    if st.button('Register New Review'):

        data_review = {
            'movie': selected_movie_title,
            'stars': stars,
            'comment': comment
        }
        movies_service.post_movies(data_review)
        st.success(f'New Review registered successfully!')

    else:
        st.warning("Please fill in all fields before registering.")
