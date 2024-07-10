from paho.mqtt import client as mqtt_client
from loguru import logger


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
        else:
            logger.error("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id, protocol=mqtt_client.MQTTv5)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


client = connect_mqtt()
client.loop_start
