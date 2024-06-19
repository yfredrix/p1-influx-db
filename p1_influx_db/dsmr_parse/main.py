from calendar import c
from collections import namedtuple
from loguru import logger
import json


def parse_dsmr_telegram(telegram):
    logger.info("Parsing telegram")
    parsed_telegram = json.loads(telegram.to_json())
    logger.info("Data to write:")
    electricity_measurement = {
        "measurement": "electricity",
        "tags": {
            "unit": "kWh",
            "equipment_id": parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"],
        },
        "fields": {},
        "time": parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"],
    }
    for key in [
        "ELECTRICITY_USED_TARIFF_1",
        "ELECTRICITY_USED_TARIFF_2",
        "ELECTRICITY_DELIVERED_TARIFF_1",
        "ELECTRICITY_DELIVERED_TARIFF_2",
    ]:
        if key not in parsed_telegram:
            logger.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "kWh":
            logger.error("Unit is not kWh")
            continue
        electricity_measurement["fields"][key.lower()] = parsed_telegram[key]["value"]

    electricity_flow = {
        "measurement": "electricity_current",
        "tags": {
            "unit": "kW",
            "actief_tarief": parsed_telegram["ELECTRICITY_ACTIVE_TARIFF"]["value"],
            "equipment_id": parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"],
        },
        "fields": {},
        "time": parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"],
    }
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
            logger.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "kW":
            logger.error("Unit is not kW")
            continue
        electricity_flow["fields"][key.lower()] = parsed_telegram[key]["value"]

    voltages = {
        "measurement": "voltage",
        "tags": {
            "unit": "V",
            "equipment_id": parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"],
        },
        "fields": {},
        "time": parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"],
    }
    for key in [
        "INSTANTANEOUS_VOLTAGE_L1",
        "INSTANTANEOUS_VOLTAGE_L2",
        "INSTANTANEOUS_VOLTAGE_L3",
    ]:
        if key not in parsed_telegram:
            logger.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "V":
            logger.error("Unit is not V")
            continue
        voltages["fields"][key.lower()] = parsed_telegram[key]["value"]

    currents = {
        "measurement": "current",
        "tags": {
            "unit": "A",
            "equipment_id": parsed_telegram["EQUIPMENT_IDENTIFIER"]["value"],
        },
        "fields": {},
        "time": parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"],
    }

    for key in [
        "INSTANTANEOUS_CURRENT_L1",
        "INSTANTANEOUS_CURRENT_L2",
        "INSTANTANEOUS_CURRENT_L3",
    ]:
        if key not in parsed_telegram:
            logger.error("Key not in telegram")
            continue
        if parsed_telegram[key]["unit"] != "A":
            logger.error("Unit is not A")
            continue
        currents["fields"][key.lower()] = parsed_telegram[key]["value"]

    gas = {
        "measurement": "gas",
        "tags": {
            "unit": "m3",
            "equipment_id": parsed_telegram["EQUIPMENT_IDENTIFIER_GAS"]["value"],
        },
        "fields": {},
        "time": parsed_telegram["P1_MESSAGE_TIMESTAMP"]["value"],
    }
    if "HOURLY_GAS_METER_READING" in parsed_telegram:
        gas["fields"]["hourly"] = parsed_telegram["HOURLY_GAS_METER_READING"]["value"]

    coupledFormat = namedtuple("coupledFormat", ["topic", "payload"])
    info_list = [
        coupledFormat(topic="latest_energy", payload=electricity_measurement),
        coupledFormat(topic="latest_energy_current", payload=electricity_flow),
        coupledFormat(topic="latest_voltage_current", payload=voltages),
        coupledFormat(topic="latest_voltage_current", payload=currents),
        coupledFormat(topic="latest_gas", payload=gas),
    ]
    return info_list
