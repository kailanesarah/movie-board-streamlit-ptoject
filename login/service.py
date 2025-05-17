import streamlit as st
from api.service import Auth


def login(username, password):
    # instancia o objeto da classe de autenticação
    auth_login = Auth()

    response = auth_login.get_token(
        username=username,
        password=password
    )

    if response.get('error'):
        st.error(f'Falha ao tentar fazer login {response.get('error')}')
    else:
        # basicamente é assim, se não der erro a aplicação nos retorna um json com acesso e token
        # aí nós precisamos pegar o que nos interessa que é o acesso e guardar em um estado de sessão, na variavel token
        # Session state" (estado de sessão) é um termo usado em programação para descrever dados que são armazenados durante
        # a interação de um usuário com uma aplicação, normalmente entre várias requisições

        st.session_state.token = response.get('access')
        st.rerun()  # vai recarregar


def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()
