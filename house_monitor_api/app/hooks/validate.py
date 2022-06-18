from typing import Callable, Type
import falcon
import pydantic


def validate_json(model: Type[pydantic.BaseModel]) -> Callable:
    def wrapped(wrapped_fn: Callable):
        def wrapped_hook(request: falcon.Request, *_, **__) -> None:
            if not request.context.json:
                raise falcon.HTTPBadRequest
            
            try:
                request.context.content = model(**request.context.json)
            except pydantic.ValidationError as error:
                raise falcon.HTTPBadRequest("Validation error(s)", str(error))
                
        return falcon.before(wrapped_hook)(wrapped_fn)
    return wrapped
