from rest_framework.authentication import TokenAuthentication
from shoes.Models.Token import Token


class TokenAuthentication(TokenAuthentication):
    model = Token
