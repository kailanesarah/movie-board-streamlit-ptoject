import streamlit as st
import requests
from login.service import logout


class GenreRepository:
    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__genre_url = f"{self.__base_url}genres/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_genre(self):
        try:
            response = requests.get(self.__genre_url, headers=self.__headers)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None
            else:
                raise Exception(
                    f"Unexpected error from the genre API. "
                    f"HTTP Status Code: {response.status_code} - {response.text}"
                )

        except Exception as e:
            raise Exception(f"Error while trying to access the API: {str(e)}")

    def post_genre(self, genre):
        try:
            response = requests.post(self.__genre_url, headers=self.__headers, data=genre)

            if response.status_code == 201:
                return f"Genre successfully created! {response.json()}"
            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None

            raise Exception(
                f"Error while trying to access the API. "
                f"HTTP Status Code: {response.status_code} - {response.text}"
            )
        except Exception as e:
            raise Exception(f"Error while trying to create genre: {str(e)}")
