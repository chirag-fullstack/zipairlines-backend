# ZipAirlines

## prerequisites:
 - `python3` 
 - `virtualenv`


## Run

`python3` and `virtualenv`:
```sh

virtualenv -p python3 venv
. venv/bin/activate
cd zipairlines-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or use `docker`:
```sh
cd zipairlines-backend
docker build -t zipairlines-backend .
docker run -t -i -p 8000:8000 zipairlines-backend
```


## APIs Details

Calculate the total airplane fuel consumption per minute and maximum minutes able to fly.

```
Url: `http://localhost:8000/api/v1/airlines/airplanes/`

Endpoint: '/api/v1/airlines/airplanes/'

Method: POST
```

POST data:
```json
{
  "airplanes": [
  	{
      "id": 1,
      "passengers": 100
    },
    {
      "id": 2,
      "passengers": 200
    },
    {
      "id": 3,
      "passengers": 300
    },
    {
      "id": 4,
      "passengers": 300
    }
  ]
}
```

Response data:
```json
{
  "airplanes": [
    {
      "id": 1,
      "passengers": 100,
      "tank_capacity": 200.0,
      "per_passenger_consumption": 0.2,
      "per_minute_fuel_consumption": 1.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 20.8
    },
    {
      "id": 2,
      "passengers": 200,
      "tank_capacity": 400.0,
      "per_passenger_consumption": 0.4,
      "per_minute_fuel_consumption": 2.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 81.6
    },
    {
      "id": 3,
      "passengers": 300,
      "tank_capacity": 600.0,
      "per_passenger_consumption": 0.6,
      "per_minute_fuel_consumption": 3.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 182.4
    },
    {
      "id": 4,
      "passengers": 300,
      "tank_capacity": 800.0,
      "per_passenger_consumption": 0.6,
      "per_minute_fuel_consumption": 3.8,
      "max_fly_minutes": 210.526,
      "fuel_required": 183.2
    }
  ]
}
```


### Tests
```sh
python manage.py test
```