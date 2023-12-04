from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from knox.models import AuthToken
from knox.settings import CONSTANTS
from urllib.parse import parse_qs

@database_sync_to_async
def get_user(token):
    try:
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        return user.user
    except AuthToken.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        query_string = scope.get("query_string", b"").decode()
        query_params = parse_qs(query_string)
        token_key = query_params.get("auth", [""])[0] 
        if token_key:
            scope['user'] = await get_user(token_key)
        return await super().__call__(scope, receive, send)