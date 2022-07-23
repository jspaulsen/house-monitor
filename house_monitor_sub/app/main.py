from app import config
from app.logging import setup_logging
from app.mqtt import MQTTClient


def main() -> None:
    missing_configuration = config.missing_configuration()

    if missing_configuration:
        raise Exception(f"Missing necessary {missing_configuration} environment variables")

    setup_logging()

    client = MQTTClient()
    client.connect()
    client.loop_forever()


if __name__ == '__main__':
    main()
