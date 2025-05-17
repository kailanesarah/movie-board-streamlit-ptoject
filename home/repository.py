import streamlit as st
import requests
from login.service import logout


class MoviesStatesRepository():

    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__movies_states_url = f"{self.__base_url}movies/states/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movies_states(self):
        try:
            response = requests.get(self.__movies_states_url, headers=self.__headers)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None
            else:
                raise Exception(
                    f"Unexpected error from the states API. "
                    f"HTTP Status Code: {response.status_code} - {response.text}")
        except Exception as e:
            raise Exception(f"Error while trying to access the API: {str(e)}")
