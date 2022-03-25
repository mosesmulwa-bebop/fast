## Author
[Moses Mulwa](https://github.com/mosesmulwa-bebop)

## Included
1. Readme which details operation(This one)


### Main features

* Get List of Supported Currencies
* Get Historical Exchange Rate for desired dates
* Get Conversions for any currency
* source data is fetched via [https://www.currencyconverterapi.com/](https://www.currencyconverterapi.com/)


### Endpoints

|Method|URL|Path Params|Description|
|------|---|------|-----------|
|**GET**|`/convert`|`:from/:to/:amount` _(all required)_|Currencies convert Route|
|**GET**|`/currencies`|`/` |Supported Currencies Route|
|**GET**|`/historical`|`:from/:to/:date` _(all required)_|Historical Rate Route|



## Getting Started

### Prerequisites

* [Docker](https://docker.com) 


### Installation

1. Get a free API Key at [https://www.currencyconverterapi.com/](https://www.currencyconverterapi.com/)

2. Go to the project directory
   ```shell script
   cd currencies-converter-fastapi/
   ```
3. Setup your `.env`
   ```shell script
   API_KEY=[YOUR_API_KEY_HERE]
   ```

4. Run the service
   ```shell script
   docker build -t fast .
   docker-compose up -d
   ```



## Usage
### With Unicorn
```shell script
uvicorn app.main:app --reload
```
### General usage
### 1. List of Supported Currencies
```shell script
curl -X GET "http://127.0.0.1:8000/currencies"
```
It includes an optional start and stop command if returning all supported currencies is not desired


```shell script
curl -X GET "http://127.0.0.1:8000/currencies?start=20&stop=30"
```



##### Response (Code 200)

```json
{
    "Currencies": [
        "OMR",
        "PGK",
        "RWF",
        "WST",
        "RSD",
        "SEK",
        "TZS",
        "AMD",
        "BSD",
        "BAM"
    ]
}
```

### 2. Convert Currencies

```shell script
curl -X GET "http://127.0.0.1:8000/convert/?from_curr=USD&to_curr=KES&value_to_convert=100.89"
```



##### Response (Code 200)

```json
{
    "From": "USD",
    "To": "KES",
    "Value": 100.89,
    "Rate": 114.803804,
    "Converted": 11582.55578556
}
```
### 3. Historical Exchange Rates
_Please Note:_ The free version only allows exchange rates up to one year back.

_Note_: If curl fails,try pasting into your browser or use a dedicated tool like Postman

```shell script
curl -X GET "http://127.0.0.1:8000/historical/?base_curr=USD&target_curr=KES&date_string=2021-06-07"
```



##### Response (Code 200)

```json
{
    "From": "USD",
    "To": "KES",
    "Date": "2021-06-07",
    "Rate": 107.897997
}
```


## Documentation


### Interactive API documentation (provided by Swagger UI)

Go to `/docs` to see the automatic interactive API documentation.



### ReDoc

Go to `/redoc` to see the ReDoc documentation.


## Configuration

All application settings are stored in `.env` file.



```shell script
API_KEY=[YOUR_API_KEY]
```






## Built With

* [Python](https://www.python.org)
* [FastAPI](https://fastapi.tiangolo.com)
* [Pydantic](https://pydantic-docs.helpmanual.io)
* [Uvicorn](https://www.uvicorn.org)




## Contact

Moses Mulwa - [Moses Mulwa](https://github.com/mosesmulwa-bebop) - mosesmulwa123@gmail.com

