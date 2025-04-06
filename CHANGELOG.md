# CHANGELOG


## v2.3.1 (2025-04-06)

### Bug Fixes

- Topic definition to prevent longer topics by retries
  ([`18991b5`](https://github.com/yfredrix/p1-influx-db/commit/18991b5cd0bce76628fb764ab92c23db898a1ddd))


## v2.3.0 (2025-04-06)

### Features

- Added retry behaviour by missing network ([#7](https://github.com/yfredrix/p1-influx-db/pull/7),
  [`9fb6862`](https://github.com/yfredrix/p1-influx-db/commit/9fb6862b30ebce98340e5eabc5ab75614e2e9308))

* feat: Implement reconnect logic for MQTT client on dead queue presence

* feat: Use built in functionality to retry on disconnect

* fix: Refactor import statements for MessageStore in MQTT client

* fix: change circulair import

* fix: recursion issues

* fix: Add MQTT client connection and disconnection handlers

* feat: Implement reconnect loop with retry mechanism for MQTT client

* fix: Adjust reconnect loop to limit attempts and improve error handling

* fix: Allow reconnection for 5 minutes and use the correct topic

* fix: validate times

Temporary block after 2 times

* fix: Stop and loop stop on failed reconnection attempts

* fix: Log reconnection attempts in reconnect loop

* fix: Add exception handling for threading and improve error logging

* fix: Enhance exception handling in MQTT client to raise detailed errors

* fix: Update reconnect logic to allow more attempts and improve error handling

* fix: Change exit method on failed reconnection to use os._exit for immediate termination


## v2.2.0 (2025-04-06)

### Chores

- Added action permissions
  ([`5ca757a`](https://github.com/yfredrix/p1-influx-db/commit/5ca757aee84f33300e51a3279341c4d30c303650))

- **deps-dev**: Bump black in the pip group across 1 directory
  ([#5](https://github.com/yfredrix/p1-influx-db/pull/5),
  [`9b8baf3`](https://github.com/yfredrix/p1-influx-db/commit/9b8baf372f812cd0fe9e8637a3f25ca084ee8101))

Bumps the pip group with 1 update in the / directory: [black](https://github.com/psf/black).

Updates `black` from 23.12.1 to 24.3.0 - [Release notes](https://github.com/psf/black/releases) -
  [Changelog](https://github.com/psf/black/blob/main/CHANGES.md) -
  [Commits](https://github.com/psf/black/compare/23.12.1...24.3.0)

--- updated-dependencies: - dependency-name: black dependency-type: direct:development

dependency-group: pip ...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Features

- Added the opportunity for a dead queue for losing connection to the broker
  ([#6](https://github.com/yfredrix/p1-influx-db/pull/6),
  [`5bdf3f2`](https://github.com/yfredrix/p1-influx-db/commit/5bdf3f291622b632e8eebfaf97e9a39ebe3adcd9))


## v2.1.0 (2025-03-23)

### Features

- Added validation of config file
  ([`443105e`](https://github.com/yfredrix/p1-influx-db/commit/443105e42f7f0f5b3684055b7d45304982ad7a29))


## v2.0.0 (2025-03-22)

### Bug Fixes

- Removed uselesss import
  ([`3d9e62e`](https://github.com/yfredrix/p1-influx-db/commit/3d9e62e935e22e8b41a999384a3c51098263fd6b))

Within the main http file an automatic import was made which had no reason to be there

BREAKING CHANGE: configs are now required

### Breaking Changes

- Configs are now required


## v1.5.2 (2025-03-22)

### Break

- Updated semantic versioning
  ([`26f08cb`](https://github.com/yfredrix/p1-influx-db/commit/26f08cbfa2b8e928b12f03d9a78ce77f7814df0e))

### Breaking Change

- Fix version
  ([`db4c610`](https://github.com/yfredrix/p1-influx-db/commit/db4c610702dbbd96b09e0a2c1cd30a749f40ed18))

- New config approach
  ([`51415d4`](https://github.com/yfredrix/p1-influx-db/commit/51415d49668759154d4931f8aac65e448a7e2e76))

- Use config for value determination
  ([`45448d2`](https://github.com/yfredrix/p1-influx-db/commit/45448d270290940f1d8fc671b3ee7ece0166b362))

### Bug Fixes

- Added a log clause
  ([`8e1c4a9`](https://github.com/yfredrix/p1-influx-db/commit/8e1c4a96eb9e816a842764e7e8c9251bd09d1326))

- Blacked the files
  ([`40eb684`](https://github.com/yfredrix/p1-influx-db/commit/40eb6846b8185e3aee372e1251fa06d835a31f92))

- Https method to influx
  ([`7adfd2f`](https://github.com/yfredrix/p1-influx-db/commit/7adfd2f4ee431bb8ca0f4a86e5bf7ebbc2f63ef9))

- Solved forgotten issue with config-file
  ([`e0b10bb`](https://github.com/yfredrix/p1-influx-db/commit/e0b10bb382ea047cf6030390d4cf3620240b84a6))

- Unittest and typo issue with keys
  ([`9a3069b`](https://github.com/yfredrix/p1-influx-db/commit/9a3069bc7ac3d48994f68a8e86390053ac9206d3))

- Updated library links
  ([`6312de7`](https://github.com/yfredrix/p1-influx-db/commit/6312de7d14e2348e4d032d44348b84e1ef002a0f))

- Updated packages
  ([`7b7758c`](https://github.com/yfredrix/p1-influx-db/commit/7b7758cf557bbe2183d12d52065539d258d94b6e))

### Chores

- Blacked files
  ([`17bc1cb`](https://github.com/yfredrix/p1-influx-db/commit/17bc1cb51bae4525ebc3495223eaf996883eb6ed))

- Updated release pipeline
  ([`2b65970`](https://github.com/yfredrix/p1-influx-db/commit/2b659707cc7bbeef6bcacc6477406a99ee0172d8))

### Documentation

- Updated readme
  ([`febce19`](https://github.com/yfredrix/p1-influx-db/commit/febce1984fc3666b6b1c8eb342be9132b6abea22))


## v1.5.1 (2025-03-22)

### Bug Fixes

- Reduced timeout
  ([`36a983f`](https://github.com/yfredrix/p1-influx-db/commit/36a983fd55fb63b7388035387e5b4a39ec486977))

### Chores

- Added black configuration to pyproject.toml
  ([`b62212d`](https://github.com/yfredrix/p1-influx-db/commit/b62212d5ee020b3563d2071570549352bab2bec3))

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
