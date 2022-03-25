api_key = "33502c63e80736700dc5"

def make_convert_url(from_curr, to_curr):
    base_url = "https://free.currconv.com/api/v7/convert?q="
    final_api_url = base_url+from_curr+"_"+to_curr+"&compact=ultra&apiKey="+api_key
    return final_api_url

def make_currencies_url():
    single_base ="https://free.currconv.com/api/v7/"
    final_currency_url = single_base+"currencies?apiKey="+api_key
    return final_currency_url

def make_historical_url(base_curr, target_curr,date_string):
    single_base ="https://free.currconv.com/api/v7/"
    final_url = single_base+"convert?q="+base_curr+"_"+target_curr+"&compact=ultra&date="+date_string+"&apiKey="+api_key
    return final_url