# CHANGELOG

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
