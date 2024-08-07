# CHANGELOG

## v1.5.0 (2024-07-21)

### Feature

* feat: Update equipment_id and time fields in parse_dsmr_telegram ([`19d3b1e`](https://github.com/yfredrix/p1-influx-db/commit/19d3b1e830255d5b0dd4abdfbf7487dda1929a92))

* feat: Removed password support ([`b834231`](https://github.com/yfredrix/p1-influx-db/commit/b83423158d544a66dead5987bf4dd5bd5b8b78e8))

* feat: Added QoS to mqtt publish ([`c45d418`](https://github.com/yfredrix/p1-influx-db/commit/c45d418aee58b8aac8c92129ec558c3da0539a30))

* feat: Added password for MQTT ([`ea130f9`](https://github.com/yfredrix/p1-influx-db/commit/ea130f9b8096c883fdd374b947624628763b11e9))

* feat: Fixed the parser of DSMR messages and sending to MQTT ([`6662abe`](https://github.com/yfredrix/p1-influx-db/commit/6662abe22b4f0a7319333ea4304b10b3fa430d94))

### Fix

* fix: work on all pcs ([`a220614`](https://github.com/yfredrix/p1-influx-db/commit/a220614f2d4f85e97ddd59f49b9db7eba88c103c))

### Refactor

* refactor: Formated files to max 127 chars ([`275c5cf`](https://github.com/yfredrix/p1-influx-db/commit/275c5cf54b340d9dd8392b540634fb10c6606c45))

* refactor: Update equipment_id and time fields in parse_dsmr_telegram

The code changes update the equipment_id and time fields in the parse_dsmr_telegram function. Instead of accessing the values using dictionary keys, the code now directly accesses the attributes of the telegram object. This improves readability and simplifies the code. ([`c9ab7f9`](https://github.com/yfredrix/p1-influx-db/commit/c9ab7f96ca80bbda9bd871d14f852a0cdac28592))

### Unknown

* Merge pull request #3 from yfredrix/parse_tests

feat: Updated the parser to work with Telegram objects; changed the QoS for MQTT ([`5ca7341`](https://github.com/yfredrix/p1-influx-db/commit/5ca734174ee0150967e1fcacad521bb9ac2f69eb))

* Add test data ([`9e1f4cc`](https://github.com/yfredrix/p1-influx-db/commit/9e1f4ccd065fa4c6db774d0e8d6ba0b3ca8ba57a))

* Changed topic ([`47ad321`](https://github.com/yfredrix/p1-influx-db/commit/47ad321cc60882f4e4787daabc6845e95b353f75))

## v1.4.0 (2024-07-20)

### Unknown

* Merge branch &#39;main&#39; of https://github.com/yfredrix/p1-influx-db ([`313ee2e`](https://github.com/yfredrix/p1-influx-db/commit/313ee2e4bb70d855efb6c4585b78339c9869268b))

## v1.3.4 (2024-07-20)

### Feature

* feat: removed logging function of on_connect ([`00de0f1`](https://github.com/yfredrix/p1-influx-db/commit/00de0f1df9fbc82ef9d1ae701b5f81d01b6bfc1e))

### Fix

* fix: Remove unused tls_insecure_set attribute in MqttClient

The code changes remove the unused tls_insecure_set attribute in the MqttClient class. This attribute is no longer needed and can be safely removed, improving the code&#39;s cleanliness and reducing unnecessary complexity. ([`2feddc3`](https://github.com/yfredrix/p1-influx-db/commit/2feddc337ca7d266eb36b76ff68ab0c899f3861f))

## v1.3.3 (2024-07-20)

### Chore

* chore: Refactor argument parsing in __main__.py ([`0a3b1c5`](https://github.com/yfredrix/p1-influx-db/commit/0a3b1c5d65c3337d6ed242cde6e6db33d8d4d60f))

### Fix

* fix: Refactor argument parsing in __main__.py

The code changes refactor the argument parsing in the __main__.py file. The unnecessary newline and indentation in the argument definition are removed, resulting in cleaner and more concise code. ([`d98fc03`](https://github.com/yfredrix/p1-influx-db/commit/d98fc0393f0bf3a7f6e642e47b2b84ec89ee26b0))

## v1.3.2 (2024-07-20)

### Chore

* chore: Refactor argument parsing in __main__.py

The code changes refactor the argument parsing in the __main__.py file. The unnecessary newline and indentation in the argument definition are removed, resulting in cleaner and more concise code. ([`7f87608`](https://github.com/yfredrix/p1-influx-db/commit/7f87608e2e09e3146267057f7c01240534dfdf0b))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/yfredrix/p1-influx-db ([`363b900`](https://github.com/yfredrix/p1-influx-db/commit/363b900ddf6e313476ea58372af237c032173fb6))

## v1.3.1 (2024-07-20)

### Fix

* fix: Remove unused imports and modules in __main__.py

The code changes remove unused imports and modules in the __main__.py file. This refactor improves the code&#39;s cleanliness and reduces unnecessary dependencies. ([`a33d807`](https://github.com/yfredrix/p1-influx-db/commit/a33d807eeae4684570661a6865330c66940d8443))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/yfredrix/p1-influx-db ([`4d9b2f5`](https://github.com/yfredrix/p1-influx-db/commit/4d9b2f544605d058bf97809f0f810a59f401ac1c))

## v1.3.0 (2024-07-20)

### Feature

* feat: Update pyproject.toml to include pydantic version 2.8.2

The code changes in the pyproject.toml file add the pydantic package with version 2.8.2 to the project&#39;s dependencies. This update is necessary to ensure compatibility with the latest version of pydantic and to leverage its features in the codebase. ([`45322c3`](https://github.com/yfredrix/p1-influx-db/commit/45322c3a5a92dbee288b02aeef2146127aac6c53))

### Fix

* fix: Remove unused imports and modules in p1_influx_db package ([`2bf9229`](https://github.com/yfredrix/p1-influx-db/commit/2bf92291f2c6392ccf212848c211449d02c086ae))

## v1.2.0 (2024-07-20)

### Chore

* chore: Update python-package.yml to include Python 3.11 setup and poetry installation

The code changes in the python-package.yml file add the setup for Python 3.11 and the installation of the poetry package manager. This update is necessary to ensure compatibility with the latest Python version and to use poetry for managing dependencies and building the package. ([`208dd89`](https://github.com/yfredrix/p1-influx-db/commit/208dd892e25a0d9fe5d0636e27d8ee3753ba67ea))

* chore: Enable automatic pushing in python-package.yml ([`ac6b89e`](https://github.com/yfredrix/p1-influx-db/commit/ac6b89e4de695cc6804e9afe92fcae4cd37c3154))

* chore: Update pydantic import in formats.py and test_main.py ([`0b6788f`](https://github.com/yfredrix/p1-influx-db/commit/0b6788f74a8cd7cc55490cdc43c6efe21f870b00))

### Feature

* feat: Refactor MQTT client and publish functionality

The code changes refactor the MQTT client and publish functionality in the `p1_influx_db` package. The `publish.py` module is removed, and its functionality is now handled by the `MqttClient` class in the `client.py` module. The `mqttmain.py` module is updated to use the new `MqttClient` class for publishing messages. This refactor improves the organization and maintainability of the MQTT functionality in the package. ([`8a31d74`](https://github.com/yfredrix/p1-influx-db/commit/8a31d74eabb44a0b0ebf2ec20817235064c35da4))

* feat: added support for mqtt ([`a527f36`](https://github.com/yfredrix/p1-influx-db/commit/a527f36d139735b4607b61f18232efa3d446607c))

* feat: added support for mqtt ([`3781cc7`](https://github.com/yfredrix/p1-influx-db/commit/3781cc74211000b5e506592682ee21132228694d))

### Refactor

* refactor: Update P1_MESSAGE_TIMESTAMP handling in test_main.py

The code changes refactor the handling of the P1_MESSAGE_TIMESTAMP field in the test_main.py module. Instead of using the datetime function to create a timestamp, the value is now directly assigned as a dictionary value. This refactor improves the readability and maintainability of the code. ([`be59666`](https://github.com/yfredrix/p1-influx-db/commit/be5966680ab3183c0718512ef9543aae3daf3d91))

* refactor: Refactor MQTT client and publish functionality in p1_influx_db package ([`b6f01db`](https://github.com/yfredrix/p1-influx-db/commit/b6f01db637e737478ba6849f6f7affbbc05a10f1))

* refactor: remove unused test_abc function ([`68981ef`](https://github.com/yfredrix/p1-influx-db/commit/68981ef39e2224c91351824e38ecd1cb1a67f1f2))

### Unknown

* Merge pull request #2 from yfredrix/mqtt

Added MQTT support for P1 reader ([`78182ce`](https://github.com/yfredrix/p1-influx-db/commit/78182ce187ca98d16b14e1752905f200aabcace9))

* Merge branch &#39;mqtt&#39; of https://github.com/yfredrix/p1-influx-db into mqtt ([`a6c3601`](https://github.com/yfredrix/p1-influx-db/commit/a6c36013f246c0c3db924c049f0fb615f553c8fe))

* feat sync mqtt ([`3794524`](https://github.com/yfredrix/p1-influx-db/commit/3794524ef7857ab90e967c6411b4455a2bedd288))

* Fixed optional dependencies ([`baea413`](https://github.com/yfredrix/p1-influx-db/commit/baea4132248184bb01b7d7f697bbce162c17040f))

* feat sync mqtt ([`6219df4`](https://github.com/yfredrix/p1-influx-db/commit/6219df4fba42b0737ad28e5afd23fedd28b9f863))

* Fixed optional dependencies ([`45102ed`](https://github.com/yfredrix/p1-influx-db/commit/45102edddde81db1b80f46da24fdc42646960471))

* Update python-package.yml ([`a59768c`](https://github.com/yfredrix/p1-influx-db/commit/a59768cd8d4320de9456f4dd62dcfc47a71346d3))

* Update python-package.yml ([`460fc85`](https://github.com/yfredrix/p1-influx-db/commit/460fc851eb0fa0ff9e5a5219d70ca41ffa85e9cf))

* Update python-package.yml ([`97ead24`](https://github.com/yfredrix/p1-influx-db/commit/97ead24bcd831fdf1d1ec24b8a181771b7546a1d))

## v1.1.0 (2024-07-10)

### Feature

* feat: Update python-package.yml ([`6009701`](https://github.com/yfredrix/p1-influx-db/commit/6009701986b030c70b0e2f4e53f9053c2eb2063e))

### Performance

* perf: Setup CI ([`33e8ffe`](https://github.com/yfredrix/p1-influx-db/commit/33e8ffe6ef57acd1eabba82d4e8082b694097728))

### Unknown

* Feat: Added CI pipeline

Create python-package.yml ([`33814a1`](https://github.com/yfredrix/p1-influx-db/commit/33814a1b33ffcbc4d85627166d998eac1f6db8de))

* Merge branch &#39;yfredrix-patch-1&#39; of https://github.com/yfredrix/p1-influx-db into yfredrix-patch-1 ([`5597cc6`](https://github.com/yfredrix/p1-influx-db/commit/5597cc6cf6e0a0d9d88afc36dd97457da5c7ed0f))

* Added dependencies and pyproject ([`9d6e1d7`](https://github.com/yfredrix/p1-influx-db/commit/9d6e1d7e11e1567478b702a3eb68b1145c49d315))

* Added fake test ([`e01a4f2`](https://github.com/yfredrix/p1-influx-db/commit/e01a4f2a3638651854488700263bf13ca8b46e76))

* Shorter line length ([`8db9f3b`](https://github.com/yfredrix/p1-influx-db/commit/8db9f3b0f62dff7746ce76120b0cd5e9f259b53e))

* Update python-package.yml ([`ce92de7`](https://github.com/yfredrix/p1-influx-db/commit/ce92de724a29014752d6d88f07b0c37769615100))

* Update python-package.yml ([`4ea413c`](https://github.com/yfredrix/p1-influx-db/commit/4ea413ce08ce91564f205f0802b4e4be5f2dc13a))

* Update python-package.yml ([`03116ea`](https://github.com/yfredrix/p1-influx-db/commit/03116eaa6bc2908d5f2fbcbb44aed5de1f050d33))

* Update python-package.yml ([`0bee1b1`](https://github.com/yfredrix/p1-influx-db/commit/0bee1b16b3525d17b9af0a57814beb3504604a44))

* Create python-package.yml ([`39caf40`](https://github.com/yfredrix/p1-influx-db/commit/39caf40b9ffc1f19d079b25edb5d3990771d28ec))

## v1.0.0 (2024-06-19)

## v0.0.0 (2024-06-19)

### Unknown

* Fix error handling in main.py ([`71b9226`](https://github.com/yfredrix/p1-influx-db/commit/71b9226edb08ef4997c38e690bb6d6458068835c))

* Refactor task creation in main.py ([`20e550e`](https://github.com/yfredrix/p1-influx-db/commit/20e550e5d05fe4a4423b69557c381ff34ac29870))

* Add error handling on top level ([`ece5ef2`](https://github.com/yfredrix/p1-influx-db/commit/ece5ef2da08dd939181a130446911390eb12898b))

* Added named parameter ([`e25c9bb`](https://github.com/yfredrix/p1-influx-db/commit/e25c9bb1a77bfac20370c56fc25d928ca5cded94))

* Refactor code to handle errors when writing to InfluxDB ([`160e431`](https://github.com/yfredrix/p1-influx-db/commit/160e431f4d1baf1381d948ffd70064c83a94b9dc))

* Refactor main.py to remove unnecessary code and improve readability ([`77736a0`](https://github.com/yfredrix/p1-influx-db/commit/77736a05faf5486812c0e1c887e4fb3811483760))

* Fix error handling in InfluxDB connection and writing ([`935586d`](https://github.com/yfredrix/p1-influx-db/commit/935586d6019df9209cc1620b0aee6ee414c9d9ed))

* Try new method for exception parsing ([`d764f5d`](https://github.com/yfredrix/p1-influx-db/commit/d764f5d9e6b365b9ddf086572968af8066d2dead))

* Updated to v1 ([`7771623`](https://github.com/yfredrix/p1-influx-db/commit/7771623541bff7b69ac6137b8fbfdeba3dcb1d12))

* Allow exceptions to move through the chain ([`913de19`](https://github.com/yfredrix/p1-influx-db/commit/913de1931c3eec8a3ac1d12091d33c2d62733dc1))

* Update dependencies in pyproject.toml and remove unused import in main.py ([`7044edd`](https://github.com/yfredrix/p1-influx-db/commit/7044eddb010253a47b2f47cd344bc702c708d44c))

* Fix asynchronous bug in main.py ([`abd01d9`](https://github.com/yfredrix/p1-influx-db/commit/abd01d91a644053a38bececdbf19eb3abea89128))

* Refactor serial_reader.read_as_object to use await ([`251d66e`](https://github.com/yfredrix/p1-influx-db/commit/251d66e91eb61f881705679b96e367a25326c249))

* Changed code to async ([`69353e8`](https://github.com/yfredrix/p1-influx-db/commit/69353e827bc2dd72529fd1b689c1db534984a20d))

* Add logging statements to main.py ([`2423dc1`](https://github.com/yfredrix/p1-influx-db/commit/2423dc1761cc5677dcc8b1a24501425b51629c3b))

* Added loguru ([`95214be`](https://github.com/yfredrix/p1-influx-db/commit/95214be1e0d1ffdc05410d7c24ef39ede42b55b6))

* Refactor code to include electricity flow, voltage, and current measurements ([`c13c5c1`](https://github.com/yfredrix/p1-influx-db/commit/c13c5c1f26470e50dee4587b1c8987613f5feaec))

* Remove unused logger and journald_handler ([`abc6a45`](https://github.com/yfredrix/p1-influx-db/commit/abc6a45da826325c4a6368bc9a7e5167a836f3ca))

* Update logging handler to use JournalHandler ([`aa3f9a1`](https://github.com/yfredrix/p1-influx-db/commit/aa3f9a162a173848e67c3b686551045a34a6e653))

* Add start.sh script to run the application ([`f39f7cc`](https://github.com/yfredrix/p1-influx-db/commit/f39f7cc4b5e7d09a995067e457f23b4a81ecf951))

* Add Journald logging handler ([`d26d68f`](https://github.com/yfredrix/p1-influx-db/commit/d26d68f819a1ac3bd6315d6d7fa89fc15c6831f4))

* Refactor code to improve readability and maintainability ([`b947941`](https://github.com/yfredrix/p1-influx-db/commit/b947941872f73dd9b1a13b43e7f54a22db3b5317))

* Add logging statements and improve code readability ([`f0f853c`](https://github.com/yfredrix/p1-influx-db/commit/f0f853cbdf547df3dbdc19dc004435cb3181791b))

* Update InfluxDB client configuration path ([`3577dcb`](https://github.com/yfredrix/p1-influx-db/commit/3577dcb17a3f043607bb0a3b49aa806fbd68fdc8))

* Add launch.json file and update InfluxDB client configuration ([`7f4dd97`](https://github.com/yfredrix/p1-influx-db/commit/7f4dd97e2bf47a98556d24ffea7dbcbea1924521))

* Update InfluxDBClient configuration in main.py ([`075cab2`](https://github.com/yfredrix/p1-influx-db/commit/075cab25d82e789cb5372db5b43cdabfa9fef38d))

* Add logging and write data to InfluxDB ([`6aedc14`](https://github.com/yfredrix/p1-influx-db/commit/6aedc146aaa8b00ee9bcdfaf6a144ac0d0a34482))

* Add InfluxDB configuration and update main.py ([`91b569e`](https://github.com/yfredrix/p1-influx-db/commit/91b569e46f33d42e3506caad28827fc7a224aac4))

* Refactor equipment_id tags in InfluxDB points ([`8d08f8f`](https://github.com/yfredrix/p1-influx-db/commit/8d08f8f47f463ad5181d211f5b411b5a513ba428))

* Fix timestamp value in main.py ([`bc532d3`](https://github.com/yfredrix/p1-influx-db/commit/bc532d385f4dc0da5332e137be948100a3bc3fb1))

* Update equipment_id in InfluxDB tags ([`0edca33`](https://github.com/yfredrix/p1-influx-db/commit/0edca33609f8c3f035783dbd7002fe1989424674))

* Add logging and modify data points for InfluxDB ([`ce43e55`](https://github.com/yfredrix/p1-influx-db/commit/ce43e554c1e922d1eef303997f192282b7b12d55))

* Refactor code to parse and print JSON data from telegram ([`81f5296`](https://github.com/yfredrix/p1-influx-db/commit/81f52963418081be39be64993c5e4769db418f17))

* Debug ([`05f758a`](https://github.com/yfredrix/p1-influx-db/commit/05f758a3375dc3916e1056fcade4d55494b9b4d9))

* Refactor code to handle POWER_EVENT_FAILURE_LOG and nested values in telegram ([`cbf8a3a`](https://github.com/yfredrix/p1-influx-db/commit/cbf8a3af65a520ba26cc0df01f450741dc76d5cc))

* Refactor print statement to use value.to_json() method ([`de0152a`](https://github.com/yfredrix/p1-influx-db/commit/de0152a891de4a7f1a8e7ceb320706d63d00e69b))

* Show values ([`0dc146b`](https://github.com/yfredrix/p1-influx-db/commit/0dc146b3be3b92218b1cb99e98a6b0711d1b472c))

* Add code to read and print DSMR telegrams ([`f089e84`](https://github.com/yfredrix/p1-influx-db/commit/f089e84234f59648d3946d7d673d3fbf5806a4de))

* Fixed to correct serial ([`a770e25`](https://github.com/yfredrix/p1-influx-db/commit/a770e25f6670bcfac977da3babf1829e3748346e))

* Update Python version and add new packages ([`f6a2306`](https://github.com/yfredrix/p1-influx-db/commit/f6a230607cc7431151d3548befdf8421de0760f0))

* Add P1 serial parsing to Influx DB ([`850b3e9`](https://github.com/yfredrix/p1-influx-db/commit/850b3e9c72b3ec41cdfa8b83db7abb8b498abd04))

* Initial commit ([`f0b889a`](https://github.com/yfredrix/p1-influx-db/commit/f0b889a673f0e318b98558b0705383aa1bbba497))
