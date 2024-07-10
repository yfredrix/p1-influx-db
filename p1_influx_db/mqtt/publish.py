from p1_influx_db.dsmr_parse import dsmrMessages
from paho.mqtt import client as mqtt_client
from .client import client
from loguru import logger


def publish(message: dsmrMessages, client: mqtt_client.Client = client):
    topic = message["topic"]
    payload = message["payload"]
    result = client.publish(topic, payload)

    status = result[0]
    if status == 0:
        logger.debug(f"Send `{payload}` to topic `{topic}`")
    else:
        logger.error(f"Failed to send message to topic {topic}")
