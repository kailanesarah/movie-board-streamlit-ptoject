import streamlit as st
from reviews.repository import ReviewsRepository


class ReviewsService():
    def __init__(self):
        self.reviews_repository = ReviewsRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.movies
        reviews = self.reviews_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def post_review(self, data_review):
        reviews = dict(
            movie=data_review.get("movie"),
            stars=data_review.get("stars"),
            comment=data_review.get("comment")
        )
        new_review = self.reviews_repository.post_review(reviews)
        st.session_state.reviews.append(new_review)
