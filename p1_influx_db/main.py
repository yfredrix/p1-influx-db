from loguru import logger
import json
import asyncio
import argparse

from dsmr_parser import telegram_specifications
from dsmr_parser.clients import AsyncSerialReader, SERIAL_SETTINGS_V5
from .dsmr_parse import parse_dsmr_telegram
from .http_to_influxdb import send_parsed_telegram
from .mqtt import publish_parsed_telegram
from aiohttp.client_exceptions import ClientConnectorError


async def parse_telegram_influx(name, queue: asyncio.Queue, config_file: str):
    while True:
        telegram = await queue.get()
        info_list = parse_dsmr_telegram(telegram)
        if method == "http":
            await send_parsed_telegram(info_list, queue, config_file)
        elif method == "mqtt":
            await publish_parsed_telegram(info_list)
        else:
            raise NotImplementedError("Method not implemented")
        queue.task_done()


async def main(config_file="./p1_influx_db/config.toml"):
    queue = asyncio.Queue()
    logger.info("Opening SerialReader")
    serial_reader = AsyncSerialReader(
        device="/dev/serial0",
        serial_settings=SERIAL_SETTINGS_V5,
        telegram_specification=telegram_specifications.V5,
    )
    tasks = []
    for i in range(3):
        tasks.append(
            asyncio.create_task(
                parse_telegram_influx(f"worker-{i}", queue, config_file=config_file)
            )
        )

    await serial_reader.read_as_object(queue)
    result = await asyncio.gather(*tasks, return_exceptions=True)
    for r in result:
        if isinstance(r, ClientConnectorError):
            raise r
        elif isinstance(r, Exception):
            raise r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="config file", default="./config.toml")
    args = parser.parse_args()

    asyncio.run(main(args.config))
