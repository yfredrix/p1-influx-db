import paho.mqtt.client as mqtt
from loguru import logger
import ssl
import time
from p1_influx_db.mqtt import MessageStore


class MqttClient(mqtt.Client):
    def __init__(self, broker, port, client_id, ca_certs, certfile, key):
        super().__init__(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
        self.broker = broker
        self.port = port
        self.client_id = client_id
        self.message_store = MessageStore()
        self.last_will = None

        self.tls_set(
            ca_certs=ca_certs,
            certfile=certfile,
            keyfile=key,
            cert_reqs=ssl.CERT_REQUIRED,
            tls_version=ssl.PROTOCOL_TLS,
        )

        self.on_connect = self.on_connect_handler
        self.on_disconnect = self.on_disconnect_handler
        self.on_publish = self.on_publish_handler

    def start(self):
        self.connect(self.broker, self.port, clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY)
        self.loop_start()

    def stop(self):
        self.loop_stop()

    def on_connect_handler(self, client, userdata, flags, rc):
        logger.debug("Connected with result code " + str(rc))
        self.resend_messages()

    def on_disconnect_handler(self, client, userdata, rc):
        logger.warning("Disconnected with result code " + str(rc))
        if rc != 0:
            logger.info("Unexpected disconnection. Attempting to reconnect...")
            self.reconnect()

    def on_publish_handler(self, client, userdata, mid):
        logger.debug(f"Message {mid} published.")

    def publish_messages(self, topic, payload):
        message_info = self.publish(topic, payload, qos=1)
        if message_info.rc == mqtt.MQTT_ERR_NO_CONN:
            logger.error("Not connected. Storing message for later.")
            self.message_store.add_message(topic, payload)
        else:
            message_info.wait_for_publish(1.5)

    def resend_messages(self):
        while True:
            message = self.message_store.get_message()
            if message is None:
                break
            topic, payload = message
            logger.info(f"Resending message to topic {topic}")
            self.publish_messages(topic, payload)
            time.sleep(1)  # Optional delay between resends

    def reconnect(self):
        while True:
            try:
                self.reconnect()
                break
            except Exception as e:
                logger.error(f"Reconnect failed: {e}")
                time.sleep(5)  # Wait before retrying to reconnect
