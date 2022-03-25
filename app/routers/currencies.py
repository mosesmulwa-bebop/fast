from fastapi import APIRouter
import requests

router  = APIRouter(
    tags = ['Currencies']
)

@router.get('/currencies')
def currencies():
    api_key = "33502c63e80736700dc5"
    single_base ="https://free.currconv.com/api/v7/"
    final_currency_url = single_base+"currencies?apiKey="+api_key
    curr_response = requests.get(final_currency_url).json()['results']
    my_curr_list = []
    for key in curr_response:
        my_curr_list.append(key)
    return {"Currencies":my_curr_list}
