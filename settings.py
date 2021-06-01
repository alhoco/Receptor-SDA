from pydantic import BaseSettings

class Settings(BaseSettings):
    MQTT_BROKER: str = "broker.hivemq.com"
    MQTT_PORT: int = 1883
    MQTT_SUBSCRIBER: str = "sda/sensor"