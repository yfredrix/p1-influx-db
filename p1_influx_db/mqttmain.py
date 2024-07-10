from loguru import logger

from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
from .dsmr_parse import parse_dsmr_telegram


def mqttmain(config_file="./p1_influx_db/config.toml"):
    logger.info("Opening SerialReader")
    serial_reader = SerialReader(
        device="/dev/serial0",
        serial_settings=SERIAL_SETTINGS_V5,
        telegram_specification=telegram_specifications.V5,
    )
    for telegram in serial_reader.read_as_object():
        info_list = parse_dsmr_telegram(telegram)
        from .mqtt import publish

        for dsmr_message in info_list:
            publish(dsmr_message)
