from fastapi import APIRouter
import requests

router  = APIRouter(
    tags = ['Currencies']
)

@router.get('/currencies')
def currencies():
    currency_api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=e5c20fa1b72ecc525b38c4540d5f4dae"
    currency_response = requests.get(currency_api_url)
    currency_response_dict = currency_response.json()
    rates_dict = currency_response_dict['rates']
    rates_list = []
    for key in rates_dict:
        rates_list.append(key)
    return {"Currencies":rates_list}