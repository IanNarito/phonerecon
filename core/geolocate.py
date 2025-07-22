import requests

def get_geolocation(phone_number):
    result = {
        "Country": "Unknown",
        "Region": "Unknown",
        "City": "Unknown"
    }

    try:
        print("[•] Fetching geolocation info...")
        API_KEY = "17cb8f2671ce41eb8da388682b94312f&phone=14152007986"
        url = f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={phone_number}"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("valid"):
            result["Country"] = data.get("country", "Unknown")
            result["Region"] = data.get("region", "Unknown")
            result["City"] = data.get("city", "Unknown")
        else:
            print("[!] Unable to validate phone number or fetch location data.")

    except Exception as e:
        print(f"[!] Geolocation lookup failed: {e}")

    return result  
