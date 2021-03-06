from fastapi import APIRouter,status, HTTPException
import requests

from ..utils import make_convert_url


router  = APIRouter(
    tags = ['Convert']
)

@router.get('/convert/')
def convert(from_curr:str, to_curr:str, value_to_convert):
    final_api_url = make_convert_url(from_curr,to_curr)
    try:
        response = requests.get(final_api_url).json()
        key_dict = from_curr+"_"+to_curr
        rate = response[key_dict]
        value_to_convert = float(value_to_convert)
        answer = rate * value_to_convert
        my_dict = {
            "From":from_curr,
            "To":to_curr,
            "Value" : value_to_convert,
            "Rate" :rate,
            "Converted": answer
        }
        #return answer
        return my_dict
    except:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                            detail=f"API Call to Currency Converter API failed")
