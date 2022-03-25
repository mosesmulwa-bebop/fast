from fastapi import APIRouter
import requests

router  = APIRouter(
    tags = ['Historical Data']
)

@router.get('/historical')
def historical():
    api_key = "33502c63e80736700dc5"
    single_base ="https://free.currconv.com/api/v7/"
    base_curr = "USD"
    target_curr = "KES"
    date_string ="2021-06-07"
    stuff="https://free.currconv.com/api/v7/convert?q=USD_KES&compact=ultra&date=2021-06-07&apiKey=33502c63e80736700dc5"
    final_url = single_base+"convert?q="+base_curr+"_"+target_curr+"&compact=ultra&date="+date_string+"&apiKey="+api_key
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