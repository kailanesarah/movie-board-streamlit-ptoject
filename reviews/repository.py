import streamlit as st
import requests
from login.service import logout


class ReviewsRepository:
    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__review_url = f"{self.__base_url}review/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_reviews(self):
        try:
            response = requests.get(self.__review_url, headers=self.__headers)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None
            else:
                raise Exception(
                    f"Unexpected error from the reviews API. "
                    f"HTTP Status Code: {response.status_code} - {response.text}"
                )
        except Exception as e:
            raise Exception(f"Error while trying to retrieve reviews: {str(e)}")

    def post_review(self, review):
        try:
            response = requests.post(
                self.__review_url, headers=self.__headers, data=review,
            )
            if response.status_code == 201:
                return f"Review successfully created! {response.json()}"

            elif response.status_code == 401:
                logout()
                st.warning("Session expired. You have been logged out.")
                return None

            raise Exception(
                f"Error while trying to create the review. "
                f"HTTP Status Code: {response.status_code} - {response.text}"
            )
        except Exception as e:
            raise Exception(f"Error while trying to create the review: {str(e)}")
