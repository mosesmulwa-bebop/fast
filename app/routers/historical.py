from fastapi import APIRouter
import requests

from ..utils import make_historical_url

router  = APIRouter(
    tags = ['Historical Data']
)

@router.get('/historical')
def historical():
    base_curr = "USD"
    target_curr = "KES"
    date_string ="2021-06-07"
    final_url = make_historical_url(base_curr, target_curr,date_string)
    historical_response = requests.get(final_url).json()
    key_dict = base_curr+"_"+target_curr
    actual_rate =historical_response[key_dict] [date_string]
    my_dict = {
        "From" : base_curr,
        "To": target_curr,
        "Date": date_string,
        "Rate" : actual_rate
    }
    return my_dict