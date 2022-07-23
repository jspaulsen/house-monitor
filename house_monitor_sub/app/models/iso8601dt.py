import pendulum


class ISO8601DateTime(pendulum.DateTime):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return pendulum.parse(v).in_tz('UTC')
