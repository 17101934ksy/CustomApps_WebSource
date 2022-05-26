import requests

def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '0baabcb6474e2bccef1ba20226d9e24e'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
 
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except:
              return 0  
    else:
        return 0
    return result