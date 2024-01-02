from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# bucket = "<my-bucket>"
# org = "<my-org>"
# token = "<my-token>"
# # Store the URL of your InfluxDB instance
# url=

# client = influxdb_client.InfluxDBClient(
#    url=url,
#    token=token,
#    org=org
# )


serial_reader = SerialReader(
    device='/dev/serial0',
    serial_settings=SERIAL_SETTINGS_V5,
    telegram_specification=telegram_specifications.V5
)


for telegram in serial_reader.read_as_object():
    for attr, value in telegram:
        print(attr)
        if attr == 'POWER_EVENT_FAILURE_LOG':
            print("POWER_EVENT_FAILURE_LOG")
            print(value)
            print(value.to_json())
            print("DONE")
        if isinstance(value, list):
            for sub_value in value:
                print(sub_value.to_json())
        else:
            print(value.to_json())
    break