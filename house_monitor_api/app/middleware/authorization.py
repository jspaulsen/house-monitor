import falcon

from app import config


class AuthorizationMiddleware:
    def process_request(self, request: falcon.Request, resposne: falcon.Response) -> None:
        auth = request.auth

        if not (auth := request.auth):
            raise falcon.HTTPUnauthorized

        try:
            api_key = auth.split("Bearer ")[1]
        except IndexError:
            raise falcon.HTTPUnauthorized
        
        if api_key != config.API_KEY:
            raise falcon.HTTPUnauthorized
        
