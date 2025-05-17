import streamlit as st
import requests
from login.service import logout


class ActorsRepository():
    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__actors_url = f"{self.__base_url}actors/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_actors(self):
        try:
            response = requests.get(self.__actors_url, headers=self.__headers)

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

    def post_actors(self, actors):
        try:
            response = requests.post(
                self.__actors_url, headers=self.__headers, data=actors)
            if response.status_code == 201:
                return f"Actor successfully created! {response.json()}"
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
