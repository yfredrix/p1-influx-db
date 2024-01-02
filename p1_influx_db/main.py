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
        if attr == 'POWER_EVENT_FAILURE_LOG':
            continue
        if isinstance(value, list):
            for sub_value in value:
                print(sub_value.to_json())
        else:
            print(value.to_json())
    break