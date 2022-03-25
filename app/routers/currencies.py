from fastapi import APIRouter,status, HTTPException

import requests

from ..utils import make_currencies_url

router  = APIRouter(
    tags = ['Currencies']
)

@router.get('/currencies')
def currencies(start:int = 0,stop:int = -1):
    final_currency_url = make_currencies_url()
    try:
        curr_response = requests.get(final_currency_url).json()['results']
        my_curr_list = []
        for key in curr_response:
            my_curr_list.append(key)
        return {"Currencies":my_curr_list[start:stop]}
    except:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, 
                            detail=f"API Call to Currency Converter API failed")
    
