import requests

class Auth:
    #urls que levam a api
    def __init__(self):
        self.__base_url = "https://api-django-rest-sj7k.onrender.com/api/v1/"
        self.__auth_url = f"{self.__base_url}token/"

    #função que pega os dados do user, envia na requisição e os guarda. APós isso verifica se tudo deu certo 
    def get_token(self, username, password):
        auth_data = {
            "username" : username,
            "password" : password
        }

        auth_response = requests.post(self.__auth_url, auth_data)

        #condiciional para ver se está tudo ok e retornar resposta
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code:{auth_response.status_code}'}


    