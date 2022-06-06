import falcon


class API(falcon.App):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
