from fastapi import APIRouter
import requests

from ..utils import make_currencies_url

router  = APIRouter(
    tags = ['Currencies']
)

@router.get('/currencies')
def currencies():
    final_currency_url = make_currencies_url()
    curr_response = requests.get(final_currency_url).json()['results']
    my_curr_list = []
    for key in curr_response:
        my_curr_list.append(key)
    return {"Currencies":my_curr_list}
