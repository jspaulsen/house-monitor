import falcon
import orjson
import pydantic


class JsonMiddleware:
    def process_request(self, request: falcon.Request, *_, **__) -> None:
        if not request.content_length or not request.content_type:
            return

        body = request.stream.read(request.content_length)
        
        if not body:
            raise falcon.HTTPBadRequest

        try:
            request.context.json = orjson.loads(body)
        except orjson.JSONEncodeError:
            raise falcon.HTTPBadRequest

    def process_response(self, request: falcon.Request, response: falcon.Response, *_, **__) -> None:
        content = getattr(response.context, 'content', None)

        if not content:
            return

        if isinstance(content, pydantic.BaseModel):
            content = content.dict()

        response.text = orjson.dumps(content)
        


