import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorsService


def show_actors():
    '''LIST NEW ACTORS'''
    actors_service = ActorsService()
    actors = actors_service.get_actors()
    st.write('Actors list')

    if actors:
        try:
            actors_df = pd.json_normalize(actors)
            AgGrid(
                data=actors_df,
                reload_data=True,
                key='actors_grid')
        except Exception as e:
            st.error(f"Error while processing actors data: {str(e)}")
    else:
        st.warning('Error: Could not display the actors list.')

    '''REGISTER NEW ACTOR'''
    st.title('Register a New Actor')

    name = st.text_input(label='First Name', placeholder='Enter the first name')
    last_name = st.text_input(label='Last Name', placeholder='Enter the last name')
    birthday = st.date_input(label='Birthday')
    nationality = st.text_input(label='Nationality', placeholder='Enter the nationality')

    if st.button('Register New Actor'):
        if name and last_name and birthday and nationality:
            data_actors = {
                'name': name,
                'last_name': last_name,
                'birthday': birthday,
                'nationality': nationality
            }
            actors_service.post_actors(data_actors)
            st.success(f'New actor "{name} {last_name}" registered successfully!')

        else:
            st.warning("Please fill in all fields before registering.")
