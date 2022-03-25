from fastapi import APIRouter,status, HTTPException
import requests

from ..utils import make_historical_url

router  = APIRouter(
    tags = ['Historical Data']
)

@router.get('/historical')
def historical(base_curr:str, target_curr:str, date_string:str):
    try:
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
    except:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                            detail=f"API Call to Currency Converter API failed")