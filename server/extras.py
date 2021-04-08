from rest_framework.response import Response
from credixco.utils import generate_access_token,generate_refresh_token



def get_token_response(user):
    response = Response()
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
    }
    return response