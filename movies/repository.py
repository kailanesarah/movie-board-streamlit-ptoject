import streamlit as st
import requests
from login.service import logout


class MoviesRepository():

    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__movies_url = f"{self.__base_url}movies/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movie(self):
        try:
            response = requests.get(self.__movies_url, headers=self.__headers)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None
            else:
                raise Exception(
                    f"Unexpected error from the genre API. "
                    f"HTTP Status Code: {response.status_code} - {response.text}")
        except Exception as e:
            raise Exception(f"Error while trying to access the API: {str(e)}")

    def post_movie(self, movies):
        try:
            response = requests.post(
                self.__actors_url, headers=self.__headers, data=movies)
            if response.status_code == 201:
                return f"Movie successfully created! {response.json()}"

            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None

            raise Exception(
                f"Error while trying to access the API. "
                f"HTTP Status Code: {response.status_code} - {response.text}"
            )
        except Exception as e:
            raise Exception(f"Error while trying to create actor: {str(e)}")
