import pytest
import pytz
import pickle

from datetime import datetime

from p1_influx_db.dsmr_parse import parse_dsmr_telegram
from dsmr_parser.objects import Telegram


def test_parse_dsmr_telegram():
    with open("tests/test_dsmr_parse/example.pkl", "rb") as f:
        telegram: Telegram = pickle.load(f)

    expected_result = [
        {
            "measurement": "electricity",
            "tags": {
                "unit": "kWh",
                "equipment_id": "4530303039313030303031363637333133",
            },
            "fields": {
                "electricity_used_tariff_1": 13356.379,
                "electricity_used_tariff_2": 12235.936,
                "electricity_delivered_tariff_1": 0.0,
                "electricity_delivered_tariff_2": 0.0,
            },
            "time": datetime(2024, 7, 21, 14, 49, 20).astimezone(pytz.utc),
        },
        {
            "measurement": "electricity_current",
            "tags": {
                "unit": "kW",
                "actief_tarief": "0001",
                "equipment_id": "4530303039313030303031363637333133",
            },
            "fields": {
                "current_electricity_usage": 0.381,
                "current_electricity_delivery": 0.0,
                "instantaneous_active_power_l1_positive": 0.381,
                "instantaneous_active_power_l1_negative": 0.0,
            },
            "time": datetime(2024, 7, 21, 14, 49, 20).astimezone(pytz.utc),
        },
        {
            "measurement": "current",
            "tags": {
                "unit": "A",
                "equipment_id": "4530303039313030303031363637333133",
            },
            "fields": {
                "instantaneous_current_l1": 2.0,
            },
            "time": datetime(2024, 7, 21, 14, 49, 20).astimezone(pytz.utc),
        },
    ]

    res = parse_dsmr_telegram(telegram)
    readable_res = [i.payload.model_dump() for i in res]
    assert readable_res == expected_result
