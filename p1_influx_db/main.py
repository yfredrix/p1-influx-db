from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import logging
import json

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
    device="/dev/serial0",
    serial_settings=SERIAL_SETTINGS_V5,
    telegram_specification=telegram_specifications.V5,
)


for telegram in serial_reader.read_as_object():
    parsed_telegram = json.loads(telegram.to_json())
    for k, v in parsed_telegram.items():
        print(k)
        print(v)
    p_elect = (
        influxdb_client.Point("electricity")
        .tag("unit", "kWh")
        .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER_ELECTRICITY"])
    )
    for key in [
        "ELECTRICITY_USED_TARIFF_1",
        "ELECTRICITY_USED_TARIFF_2",
        "ELECTRICITY_DELIVERED_TARIFF_1",
        "ELECTRICITY_DELIVERED_TARIFF_2",
    ]:
        if key not in parsed_telegram:
            logging.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "kWh":
            logging.error("Unit is not kWh")
            continue
        p_elect.field(key.lower(), parsed_telegram[key]["value"])
    p_elect.time(parsed_telegram["P1_MESSAGE_TIMESTAMP"])

    p_elect_current = (
        influxdb_client.Point("electricity_current")
        .tag("unit", "kW")
        .tag("actief_tarief", parsed_telegram["ELECTRICITY_ACTIVE_TARIFF"]["value"])
        .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER_ELECTRICITY"])
    )
    for key in [
        "CURRENT_ELECTRICITY_USAGE",
        "CURRENT_ELECTRICITY_DELIVERY",
        "INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE",
    ]:
        if key not in parsed_telegram:
            logging.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "kW":
            logging.error("Unit is not kW")
            continue
        p_elect_current.field(key.lower(), parsed_telegram[key]["value"])

    p_gas = (
        influxdb_client.Point("gas")
        .tag("unit", "m3")
        .tag("equipment_id", parsed_telegram["EQUIPMENT_IDENTIFIER_GAS"])
    )
    if "HOURLY_GAS_METER_READING" in parsed_telegram:
        p_gas.field(
            "hourly", parsed_telegram["HOURLY_GAS_METER_READING"]["value"]
        ).time(parsed_telegram["HOURLY_GAS_METER_READING"]["datetime"])
    print("Electricity:")
    print(p_elect.to_line_protocol())
    print("Electricity current:")
    print(p_elect_current.to_line_protocol())
    print("Gas:")
    print(p_gas.to_line_protocol())
    break
