from fastapi import APIRouter
import requests

from ..utils import make_convert_url

router  = APIRouter(
    tags = ['Convert']
)

@router.get('/convert')
def convert():
    to_convert = 100
    from_curr = "USD"
    to_curr = "KES"
    final_api_url = make_convert_url(from_curr,to_curr)
    response = requests.get(final_api_url).json()
    key_dict = from_curr+"_"+to_curr
    rate = response[key_dict]
    answer = rate * to_convert
    return answer
