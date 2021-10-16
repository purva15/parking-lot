# parking-lot

## Setup
Install a virtual environment with python3
```
virtualenv -p python3 venv
```
Install all required dependancies
```
pip install requirements.txt
```

## Execute

`python -m flask run`

## API Access


# API Specification
This specification defines APIs for Parking Lot Service. All the request and responses will be in JSON format

## Authentication and Authorization
Current application doesn't include any authentication and authorization requirement.

## Errors
HTTP Code `400` will be returned in case of an error in the API usage. Following parameters will be present in the response
| Key | Description | Type | Allowed Values | Required | Notes |
|-----|-------------|------|----------------|----------|-------|
|`errorId`| Unique error ID for the error | string | alphanumeric predefined values| optional | |
|`errorDescription`| Describes the error | string | | optional | |

## POST /reserve
This API is used to reserve a parking spot if available. For simplicity car is considered parked if the parking spot is available. Also, a fixed amount is charged depending on the car type.
### Request Parameters
| Key | Description | Type | Allowed Values | Required | Notes |
|-----|-------------|------|----------------|----------|-------|
|`carType`| `Type` of the car | string | `REGULAR` or `MONSTER_TRUCK` | optional | If not specified default `REGULAR` will be assumed |
|`carNo`| car Number | string | any alphanumeric value | required | If not specified `400` will be returned |

`Type` of the car can have values `REGULAR` or `MONSTER_TRUCK`

## Response Parameters

| Key | Description | Type | Allowed Values | Required | Notes |
|-----|-------------|------|----------------|----------|-------|
|`carType`| `Type` of the car | string | `REGULAR` or `MONSTER_TRUCK` | required | If not specified default `REGULAR` will be assumed |
|`carNo`| car Number | string | any alphanumeric value | required | If not specified `400` will be returned |
|`available`| availability of parking spot | boolean | `true` or `false`| required | Describes whether parking spot is available or not |
|`charge`| charge for the parking spot | Integer | $5 for `REGULAR` and `$15` for `MONSTER_TRUCK` | optional | Only when `available` is set to `true`. |
|`location`| location of the parked car | `Location` object |  | optional | Only when `available` is set to `true` |


`Location` object has following parameters
| Key | Description | Type | Allowed Values | Required | Notes |
|-----|-------------|------|----------------|----------|-------|
|`spotId`| single or multiple consecutive parking spot ids | List of Integers |  | optional |  Only when `available` is set to `true` |
|`blockId`| parking block id | Integer |  | optional |  Only when `available` is set to `true` |

### Request Example
```json
{
    "carType": "REGULAR",
    "carNo": "HWR 3886"
}
```

### Success Response Example
Example when a parking spot is available
```json
{
    "carType"; "REGULAR",
    "carNo": "HWR 3886",
    "available": true,
    "charge": 5,
    "location": {
        "spotId": [4],
        "blockId": 1
        }
}
```

Example when a parking spot is not available
```json
{
    "carType"; "MONSTER_TRUCK",
    "carNo": "HWR 3886",
    "available": false,
}
```

## GET /report
This API is used to get report of the revenue from parking lot. 

### Request Parameters
None
### Response Parameters

### Response Example
```json
{
    "totalCarsRevenueEarnedFrom" : totalCars,
	"revenue" : revenue,
    "parkedCars" : {
        "count" : totalParkedCars,
        "monster_truck" : parkedMonsterTruckCount,
        "regular" :  parkedRegularCount
    }
}	
```