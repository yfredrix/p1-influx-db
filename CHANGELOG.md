# CHANGELOG


## v1.5.1 (2025-03-22)

### Bug Fixes

- Reduced timeout
  ([`36a983f`](https://github.com/yfredrix/p1-influx-db/commit/36a983fd55fb63b7388035387e5b4a39ec486977))

### Chores

- Formatted files with line-length=127
  ([`a3382c4`](https://github.com/yfredrix/p1-influx-db/commit/a3382c4ae036bdb35e7780347e49873569d5bbde))

- Formatting updated
  ([`3bf9d7f`](https://github.com/yfredrix/p1-influx-db/commit/3bf9d7faed92b1369a991fda57251fe6ac30d455))


## v1.5.0 (2024-07-21)

### Bug Fixes

- Work on all pcs
  ([`a220614`](https://github.com/yfredrix/p1-influx-db/commit/a220614f2d4f85e97ddd59f49b9db7eba88c103c))

### Features

- Added password for MQTT
  ([`ea130f9`](https://github.com/yfredrix/p1-influx-db/commit/ea130f9b8096c883fdd374b947624628763b11e9))

- Added QoS to mqtt publish
  ([`c45d418`](https://github.com/yfredrix/p1-influx-db/commit/c45d418aee58b8aac8c92129ec558c3da0539a30))

- Fixed the parser of DSMR messages and sending to MQTT
  ([`6662abe`](https://github.com/yfredrix/p1-influx-db/commit/6662abe22b4f0a7319333ea4304b10b3fa430d94))

- Removed password support
  ([`b834231`](https://github.com/yfredrix/p1-influx-db/commit/b83423158d544a66dead5987bf4dd5bd5b8b78e8))

- Update equipment_id and time fields in parse_dsmr_telegram
  ([`19d3b1e`](https://github.com/yfredrix/p1-influx-db/commit/19d3b1e830255d5b0dd4abdfbf7487dda1929a92))

### Refactoring

- Formated files to max 127 chars
  ([`275c5cf`](https://github.com/yfredrix/p1-influx-db/commit/275c5cf54b340d9dd8392b540634fb10c6606c45))

- Update equipment_id and time fields in parse_dsmr_telegram
  ([`c9ab7f9`](https://github.com/yfredrix/p1-influx-db/commit/c9ab7f96ca80bbda9bd871d14f852a0cdac28592))

The code changes update the equipment_id and time fields in the parse_dsmr_telegram function.
  Instead of accessing the values using dictionary keys, the code now directly accesses the
  attributes of the telegram object. This improves readability and simplifies the code.


## v1.4.0 (2024-07-20)


## v1.3.4 (2024-07-20)

### Bug Fixes

- Remove unused tls_insecure_set attribute in MqttClient
  ([`2feddc3`](https://github.com/yfredrix/p1-influx-db/commit/2feddc337ca7d266eb36b76ff68ab0c899f3861f))

The code changes remove the unused tls_insecure_set attribute in the MqttClient class. This
  attribute is no longer needed and can be safely removed, improving the code's cleanliness and
  reducing unnecessary complexity.

### Features

- Removed logging function of on_connect
  ([`00de0f1`](https://github.com/yfredrix/p1-influx-db/commit/00de0f1df9fbc82ef9d1ae701b5f81d01b6bfc1e))


## v1.3.3 (2024-07-20)

### Bug Fixes

- Refactor argument parsing in __main__.py
  ([`d98fc03`](https://github.com/yfredrix/p1-influx-db/commit/d98fc0393f0bf3a7f6e642e47b2b84ec89ee26b0))

The code changes refactor the argument parsing in the __main__.py file. The unnecessary newline and
  indentation in the argument definition are removed, resulting in cleaner and more concise code.

### Chores

- Refactor argument parsing in __main__.py
  ([`0a3b1c5`](https://github.com/yfredrix/p1-influx-db/commit/0a3b1c5d65c3337d6ed242cde6e6db33d8d4d60f))


## v1.3.2 (2024-07-20)

### Chores

- Refactor argument parsing in __main__.py
  ([`7f87608`](https://github.com/yfredrix/p1-influx-db/commit/7f87608e2e09e3146267057f7c01240534dfdf0b))

The code changes refactor the argument parsing in the __main__.py file. The unnecessary newline and
  indentation in the argument definition are removed, resulting in cleaner and more concise code.


## v1.3.1 (2024-07-20)

### Bug Fixes

- Remove unused imports and modules in __main__.py
  ([`a33d807`](https://github.com/yfredrix/p1-influx-db/commit/a33d807eeae4684570661a6865330c66940d8443))

The code changes remove unused imports and modules in the __main__.py file. This refactor improves
  the code's cleanliness and reduces unnecessary dependencies.


## v1.3.0 (2024-07-20)

### Bug Fixes

- Remove unused imports and modules in p1_influx_db package
  ([`2bf9229`](https://github.com/yfredrix/p1-influx-db/commit/2bf92291f2c6392ccf212848c211449d02c086ae))

### Features

- Update pyproject.toml to include pydantic version 2.8.2
  ([`45322c3`](https://github.com/yfredrix/p1-influx-db/commit/45322c3a5a92dbee288b02aeef2146127aac6c53))

The code changes in the pyproject.toml file add the pydantic package with version 2.8.2 to the
  project's dependencies. This update is necessary to ensure compatibility with the latest version
  of pydantic and to leverage its features in the codebase.


## v1.2.0 (2024-07-20)

### Chores

- Enable automatic pushing in python-package.yml
  ([`ac6b89e`](https://github.com/yfredrix/p1-influx-db/commit/ac6b89e4de695cc6804e9afe92fcae4cd37c3154))

- Update pydantic import in formats.py and test_main.py
  ([`0b6788f`](https://github.com/yfredrix/p1-influx-db/commit/0b6788f74a8cd7cc55490cdc43c6efe21f870b00))

- Update python-package.yml to include Python 3.11 setup and poetry installation
  ([`208dd89`](https://github.com/yfredrix/p1-influx-db/commit/208dd892e25a0d9fe5d0636e27d8ee3753ba67ea))

The code changes in the python-package.yml file add the setup for Python 3.11 and the installation
  of the poetry package manager. This update is necessary to ensure compatibility with the latest
  Python version and to use poetry for managing dependencies and building the package.

### Features

- Added support for mqtt
  ([`a527f36`](https://github.com/yfredrix/p1-influx-db/commit/a527f36d139735b4607b61f18232efa3d446607c))

- Added support for mqtt
  ([`3781cc7`](https://github.com/yfredrix/p1-influx-db/commit/3781cc74211000b5e506592682ee21132228694d))

- Refactor MQTT client and publish functionality
  ([`8a31d74`](https://github.com/yfredrix/p1-influx-db/commit/8a31d74eabb44a0b0ebf2ec20817235064c35da4))

The code changes refactor the MQTT client and publish functionality in the `p1_influx_db` package.
  The `publish.py` module is removed, and its functionality is now handled by the `MqttClient` class
  in the `client.py` module. The `mqttmain.py` module is updated to use the new `MqttClient` class
  for publishing messages. This refactor improves the organization and maintainability of the MQTT
  functionality in the package.

### Refactoring

- Refactor MQTT client and publish functionality in p1_influx_db package
  ([`b6f01db`](https://github.com/yfredrix/p1-influx-db/commit/b6f01db637e737478ba6849f6f7affbbc05a10f1))

- Remove unused test_abc function
  ([`68981ef`](https://github.com/yfredrix/p1-influx-db/commit/68981ef39e2224c91351824e38ecd1cb1a67f1f2))

- Update P1_MESSAGE_TIMESTAMP handling in test_main.py
  ([`be59666`](https://github.com/yfredrix/p1-influx-db/commit/be5966680ab3183c0718512ef9543aae3daf3d91))

The code changes refactor the handling of the P1_MESSAGE_TIMESTAMP field in the test_main.py module.
  Instead of using the datetime function to create a timestamp, the value is now directly assigned
  as a dictionary value. This refactor improves the readability and maintainability of the code.


## v1.1.0 (2024-07-10)

### Features

- Update python-package.yml
  ([`6009701`](https://github.com/yfredrix/p1-influx-db/commit/6009701986b030c70b0e2f4e53f9053c2eb2063e))

### Performance Improvements

- Setup CI
  ([`33e8ffe`](https://github.com/yfredrix/p1-influx-db/commit/33e8ffe6ef57acd1eabba82d4e8082b694097728))


## v1.0.0 (2024-06-19)


## v0.0.0 (2024-06-19)
