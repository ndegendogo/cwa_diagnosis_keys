# cwa_diagnosis_keys
Python program to download and parse DEK files from the Corona Warn App server.
It loads the available daily and hourly key files from the past 14 days.
It parses the daily keys files and prints the number of keys in these files.

### Prerequisites

* A Python3 runtime environment
* Additional packages installed according to 'requirements.txt'
  (see example command-line for this using pip3 below)

### Installation

`% git clone https://github.com/ndegendogo/cwa_diagnosis_keys.git`

`% cd cwa_diagnosis_keys`

`% pip3 install -r requirements.txt`


### Usage

`python3 cwa_diagnosis_keys.py`


###Maintenance


### Data Format and References

**General:**
See [this document](https://github.com/corona-warn-app/cwa-server/blob/main/docs/DISTRIBUTION.md)
for a good overview and description of the cwa server key distribution service.

**Server URL:** 
See [this discussion](https://github.com/corona-warn-app/cwa-documentation/issues/450),
and especially [this comment](https://github.com/corona-warn-app/cwa-documentation/issues/450#issuecomment-752129355).

**Server Endpoints:** 
The endpoints and service APIs for the cwa distribution service are 
[documented here](https://github.com/corona-warn-app/cwa-server#service-apis).
Up to version 1.3, cwa got the origin country key packages (`DE` endpoints).
Since version 1.5, cwa gets the common key packages (`EUR` endpoints).
The latter packages contain also the keys from the European Federation Gateway Service.
See also [this discussion](https://github.com/corona-warn-app/cwa-documentation/issues/503).

**Key Package:** The structure of a key package was specified by Google and Apple
and is documented [here](https://developers.google.com/android/exposure-notifications/exposure-key-file-format#file-format) 
and [here](https://developer.apple.com/documentation/exposurenotification/setting_up_a_key_server).



