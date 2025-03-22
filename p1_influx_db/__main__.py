import argparse
import toml

parser = argparse.ArgumentParser()
parser.add_argument(
    "--config", help="config file", default="./p1_influx_db/example_config.toml"
)
args = parser.parse_args()

with open(args.config, "r") as f:
    config = toml.load(f)

config["p1"]["filepath"] = args.config

if "mqtt" in config:
    try:
        from p1_influx_db.mqttmain import mqttmain
    except ImportError:
        raise NotImplementedError(
            "Package install has failed; please use p1_influx_db[mqtt]"
        )
    mqttmain(config)
elif "influx2" in config:
    try:
        import asyncio
        from p1_influx_db.httpmain import mainhttp
    except ImportError:
        raise NotImplementedError(
            "Package install has failed; please use p1_influx_db[http]"
        )
    asyncio.run(mainhttp(config))
