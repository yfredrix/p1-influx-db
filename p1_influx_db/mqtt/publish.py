import asyncio
from math import e
from typing import NamedTuple
import aiomqtt
import json


async def publish(message: NamedTuple, client: aiomqtt.Client):
    topic = message["topic"]
    payload = message["payload"]
    return client.publish(topic, payload)


async def publish_parsed_telegram(telegram_list):
    """Publish the parsed telegram to the MQTT broker."""

    async with aiomqtt.Client("test.mosquitto.org") as client:
        tasks = []
        for telegram in telegram_list:
            tasks.append(publish(telegram.topic, json.dumps(telegram.payload)))

        task_results = await asyncio.gather(*tasks, return_exceptions=True)
        if not any(isinstance(task_results, Exception)):
            return True
        else:
            return False
