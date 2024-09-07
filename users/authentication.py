from typing import Optional, Tuple
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import Token

from rest_framework_simplejwt.authentication import AuthUser, JWTAuthentication

from users.unums import TokenType
from users.services import TokenService

User = get_user_model()

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Optional[Tuple[AuthUser, Token]]:
        header = self.get_header(request)
        if header in None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token in None:
            return None

        user, access_token = super().authenticate(request)
        if not self.is_validate_access_token(user, access_token):
            raise AuthenticationFailed("Access token yaroqsiz")

        return user, access_token

    @classmethod
    def is_validate_access_token(cls, user: User, access_token: Token) -> bool:
        validate_access_tokens = TokenService.get_validate_tokens(user.id, TokenType.ACCESS)
        if (
            validate_access_tokens
            and str(access_token).encode() not in validate_access_tokens
        ):
            raise AuthenticationFailed("Kirish ma'lumotlari yaroqsiz")
        return True

    