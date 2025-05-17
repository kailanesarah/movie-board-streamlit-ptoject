import streamlit as st
from actors.repository import ActorsRepository


class ActorsService():
    def __init__(self):
        self.actors_repository = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors

        actors = self.actors_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def post_actors(self, data_actors):
        actors = dict(
            name=data_actors.get("name"),
            last_name=data_actors.get("last_name"),
            birthday=data_actors.get("birthday"),
            nationality=data_actors.get("nationality"),
        )

        new_actor = self.actors_repository.post_actors(actors)
        st.session_state.actors.append(new_actor)
        return new_actor
