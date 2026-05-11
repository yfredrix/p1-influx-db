# p1-influx-db

Python package for reading DSMR/P1 telegrams from a smart meter and publishing the parsed values either to InfluxDB 2 over HTTP or to an MQTT broker.

## What it does

The package exposes a module named `p1_influx_db` that reads telegrams from the configured serial device, parses the selected DSMR values, and forwards them using one of these output modes:

- `influx2`: write parsed measurements to InfluxDB 2 using the HTTP API
- `mqtt`: publish parsed measurements as JSON messages over MQTT

The active behavior is driven by a TOML configuration file. A packaged example is available at [p1_influx_db/example_config.toml](p1_influx_db/example_config.toml).

## Requirements

- Python 3.11 or newer
- Access to the P1 serial device exposed by your meter
- One configured output target: InfluxDB 2 or MQTT

## Installation

Install from PyPI:

```bash
pip install p1-influx-db
```

Install from source with Poetry:

```bash
python -m poetry install
```

The project metadata currently defines `mqtt`, `influxdb`, and `publishmethods` extras, but the base install already includes both transport dependencies.

## Running

Run the module with an explicit config file:

```bash
python -m p1_influx_db --config /path/to/config.toml
```

If `--config` is omitted, the module falls back to `./p1_influx_db/example_config.toml`.

## Configuration

The config file must contain:

- a `[p1]` section with the serial device settings
- either an `[influx2]` section or an `[mqtt]` section

If both `[mqtt]` and `[influx2]` are present, the current entrypoint selects MQTT first.

All `keys` entries under `[p1.*]` should match DSMR field names exposed by `dsmr-parser`, such as `ELECTRICITY_USED_TARIFF_1` or `INSTANTANEOUS_VOLTAGE_L1`.

Example configuration:

```toml
# TOML-based config
[influx2]
url = "http://localhost:8086"
org = "my-org"
token = "my-token"

[mqtt]
broker = "localhost"
port = 433
client_id = "client_id"
ca_certs = "/etc/certificate/abc"
certfile = "/etc/certificate/abc"
key = "etc/certificate/key"
max_times = 60

[p1]
device = "/dev/serial0"

[p1.electricity]
keys = ["ELECTRICITY_USED_TARIFF_1",
        "ELECTRICITY_USED_TARIFF_2",
        "ELECTRICITY_DELIVERED_TARIFF_1",
        "ELECTRICITY_DELIVERED_TARIFF_2"]

[p1.electricity_current]
keys = ["CURRENT_ELECTRICITY_USAGE",
        "CURRENT_ELECTRICITY_DELIVERY",
        "INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE",
        "INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE"]

[p1.voltage]
keys = ["INSTANTANEOUS_VOLTAGE_L1",
        "INSTANTANEOUS_VOLTAGE_L2",
        "INSTANTANEOUS_VOLTAGE_L3"]

[p1.current]
keys = ["INSTANTANEOUS_CURRENT_L1",
        "INSTANTANEOUS_CURRENT_L2",
        "INSTANTANEOUS_CURRENT_L3"]

[p1.gas]
keys = ["HOURLY_GAS_METER_READING"]
```

### Output behavior

- InfluxDB mode reads the `influx2` configuration from the same TOML file and writes parsed measurements asynchronously.
- MQTT mode publishes JSON payloads under topics prefixed with `p1/`.
- MQTT TLS certificates are required by the current client implementation because TLS is always enabled.