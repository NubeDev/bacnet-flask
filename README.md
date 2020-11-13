# bacnet-flask


## to run a file that imports other classes
```
PYTHONPATH=. python server/bac_server.py

```

```
cd bacnet-flask/
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```


using bacstack to test
```
read presentValue
./bacrp 123 4 1 85
read array
./bacrp 123 4 1 87
Write a value to @16 of 1
./bacwp 123 4 1 85 16 -1 9 1
Write a value to @16 of null
./bacwp 123 4 1 85 16 -1 0 0
```



## HTTP GET:
Will return all the points
```
/api/bacnet/points
```

Will return all the a point when the UUID is passed in
```
/api/bacnet/points/<uuid>
```





## HTTP POST:
Add a new point
```
/api/bacnet/points
```
body:
```
{
  "object_type": "analogOutput",
  "object_name": "object_name",
  "address": 1,
  "relinquish_default": 1,
  "priority_array_write": {
    "_1": null,
    "_2": null,
    "_3": null,
    "_4": null,
    "_5": null,
    "_6": null,
    "_7": null,
    "_8": 99.9,
    "_9": 892.02,
    "_10": null,
    "_11": null,
    "_12": null,
    "_13": null,
    "_14": null,
    "_15": null,
    "_16": 16.9089
  },
  "units": "volts",
  "description": "description",
  "enable": true,
  "fault": false,
  "data_round": 2,
  "data_offset": 16
}

```



## HTTP PUT:
Update an existing point
```
/api/bacnet/points/<uuid>
```

body:
```
{
  "object_type": "analogOutput",
  "object_name": "object_name",
  "address": 1,
  "relinquish_default": 1,
  "priority_array_write": {
    "_1": null,
    "_2": null,
    "_3": null,
    "_4": null,
    "_5": null,
    "_6": null,
    "_7": null,
    "_8": 99.9,
    "_9": 892.02,
    "_10": null,
    "_11": null,
    "_12": null,
    "_13": null,
    "_14": null,
    "_15": null,
    "_16": 16.9089
  },
  "units": "volts",
  "description": "description",
  "enable": true,
  "fault": false,
  "data_round": 2,
  "data_offset": 16
}

```