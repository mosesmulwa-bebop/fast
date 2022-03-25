import requests
access_key = "e5c20fa1b72ecc525b38c4540d5f4dae"
api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=e5c20fa1b72ecc525b38c4540d5f4dae&symbols=USD,GBR,KES,JPY"

# response  =requests.get(api_url)
# response_dict = response.json()
# print(response_dict['rates'])

#all available currencies
currency_api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=e5c20fa1b72ecc525b38c4540d5f4dae"
currency_response = requests.get(currency_api_url)
currency_response_dict = currency_response.json()
rates_dict = currency_response_dict['rates']
rates_list = []
for key in rates_dict:
    rates_list.append(key)
#print(rates_list)

#historical 
#// "historical" endpoint - request historical rates for a specific day
base_url ="http://api.exchangeratesapi.io/v1/"
date_string = "2020-06-07"
access_key = "e5c20fa1b72ecc525b38c4540d5f4dae"
symbols = "KES"
final_historical_url = base_url+date_string+"?access_key="+access_key+"&symbols="+symbols
historical_api_url = "http://api.exchangeratesapi.io/v1/2020-06-07?access_key=e5c20fa1b72ecc525b38c4540d5f4dae&symbols=KES"
historical_response = requests.get(final_historical_url)
print(historical_response.json())

