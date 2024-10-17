import requests

def fetch_current_price():
    url = "https://api.spot-hinta.fi/JustNowRanksAndPrice"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Current Price Data:", data)
    else:
        print("Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    fetch_current_price()
