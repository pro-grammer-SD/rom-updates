import requests

def gcr(inr: int) -> int:
    url = "https://open.er-api.com/v6/latest/INR"
    data = requests.get(url).json()
    usd = data['rates']['USD']
    converted = inr*usd
    return converted
