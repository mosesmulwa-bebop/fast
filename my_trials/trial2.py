import requests

api_key = "33502c63e80736700dc5"
base_url = "https://free.currconv.com/api/v7/convert?q="
single_base ="https://free.currconv.com/api/v7/"
final_list_url = ""
to_convert = 100
from_curr = "USD"
to_curr = "KES"
final_api_url = base_url+from_curr+"_"+to_curr+"&compact=ultra&apiKey="+api_key

#api_url = "https://free.currconv.com/api/v7/convert?q=USD_KES&compact=ultra&apiKey=33502c63e80736700dc5"

response = requests.get(final_api_url).json()
key_dict = from_curr+"_"+to_curr
rate = response[key_dict]
answer = rate * to_convert
print(answer)
