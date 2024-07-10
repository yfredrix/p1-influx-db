import pytest
from p1_influx_db.dsmr_parse import parse_dsmr_telegram


def test_parse_dsmr_telegram():
    telegram = {
        "EQUIPMENT_IDENTIFIER": {"value": "123456789"},
        "P1_MESSAGE_TIMESTAMP": {"value": "2022-01-01T00:00:00Z"},
        "ELECTRICITY_ACTIVE_TARIFF": {"value": "1"},
        "ELECTRICITY_USED_TARIFF_1": {"unit": "kWh", "value": 10},
        "ELECTRICITY_USED_TARIFF_2": {"unit": "kWh", "value": 20},
        "ELECTRICITY_DELIVERED_TARIFF_1": {"unit": "kWh", "value": 30},
        "ELECTRICITY_DELIVERED_TARIFF_2": {"unit": "kWh", "value": 40},
        "CURRENT_ELECTRICITY_USAGE": {"unit": "kW", "value": 5},
        "CURRENT_ELECTRICITY_DELIVERY": {"unit": "kW", "value": 3},
        "INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE": {"unit": "kW", "value": 2},
        "INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE": {"unit": "kW", "value": 1},
        "INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE": {"unit": "kW", "value": 3},
        "INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE": {"unit": "kW", "value": 0},
        "INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE": {"unit": "kW", "value": 0},
        "INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE": {"unit": "kW", "value": 0},
        "INSTANTANEOUS_VOLTAGE_L1": {"unit": "V", "value": 220},
        "INSTANTANEOUS_VOLTAGE_L2": {"unit": "V", "value": 230},
        "INSTANTANEOUS_VOLTAGE_L3": {"unit": "V", "value": 240},
        "INSTANTANEOUS_CURRENT_L1": {"unit": "A", "value": 10},
        "INSTANTANEOUS_CURRENT_L2": {"unit": "A", "value": 15},
        "INSTANTANEOUS_CURRENT_L3": {"unit": "A", "value": 20},
        "EQUIPMENT_IDENTIFIER_GAS": {"value": "987654321"},
        "HOURLY_GAS_METER_READING": {"unit": "m3", "value": 50},
    }

    expected_result = [
        {
            "measurement": "electricity",
            "tags": {"unit": "kWh", "equipment_id": "123456789"},
            "fields": {
                "electricity_used_tariff_1": 10,
                "electricity_used_tariff_2": 20,
                "electricity_delivered_tariff_1": 30,
                "electricity_delivered_tariff_2": 40,
            },
            "time": "2022-01-01T00:00:00Z",
        },
        {
            "measurement": "electricity_current",
            "tags": {
                "unit": "kW",
                "actief_tarief": "1",
                "equipment_id": "123456789",
            },
            "fields": {
                "current_electricity_usage": 5,
                "current_electricity_delivery": 3,
                "instantaneous_active_power_l1_positive": 2,
                "instantaneous_active_power_l2_positive": 1,
                "instantaneous_active_power_l3_positive": 3,
                "instantaneous_active_power_l1_negative": 0,
                "instantaneous_active_power_l2_negative": 0,
                "instantaneous_active_power_l3_negative": 0,
            },
            "time": "2022-01-01T00:00:00Z",
        },
        {
            "measurement": "voltage",
            "tags": {"unit": "V", "equipment_id": "123456789"},
            "fields": {
                "instantaneous_voltage_l1": 220,
                "instantaneous_voltage_l2": 230,
                "instantaneous_voltage_l3": 240,
            },
            "time": "2022-01-01T00:00:00Z",
        },
        {
            "measurement": "current",
            "tags": {"unit": "A", "equipment_id": "123456789"},
            "fields": {
                "instantaneous_current_l1": 10,
                "instantaneous_current_l2": 15,
                "instantaneous_current_l3": 20,
            },
            "time": "2022-01-01T00:00:00Z",
        },
        {
            "measurement": "gas",
            "tags": {"unit": "m3", "equipment_id": "987654321"},
            "fields": {"hourly_gas_meter_reading": 50},
            "time": "2022-01-01T00:00:00Z",
        },
    ]

    assert parse_dsmr_telegram(telegram) == expected_result
