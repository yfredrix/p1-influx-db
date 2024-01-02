from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5


serial_reader = SerialReader(
    device='/dev/serial0',
    serial_settings=SERIAL_SETTINGS_V5,
    telegram_specification=telegram_specifications.V5
)


for telegram in serial_reader.read_as_object():
    for attr, value in telegram:
        print(attr)
        print(value.to_json())
    break