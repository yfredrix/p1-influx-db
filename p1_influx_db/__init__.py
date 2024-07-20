from loguru import logger
from .httpmain import httpmain
from .mqttmain import mqttmain

try:
    import paho.mqtt.client

    method = "mqtt"
except ImportError:
    logger.warning("Not running in mqtt method")
    try:
        import influxdb_client

        method = "http"
    except ImportError:
        logger.critical("No method is available; fix package installation")
        raise NotImplementedError("No method available")
