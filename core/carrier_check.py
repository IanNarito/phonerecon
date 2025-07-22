import requests

def get_carrier_info(phone_number):
    result = {
        "Valid": False,
        "Carrier": "Unknown",
        "Line Type": "Unknown"
    }

    try:
        print("[•] Fetching carrier info...")
        API_KEY = "1c7cc8262d88a5c663839e4f4d46e5e9"  # Replace this with your actual NumVerify API key
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}"

        response = requests.get(url)
        data = response.json()

        if data.get("valid"):
            result["Valid"] = True
            result["Carrier"] = data.get("carrier", "Unknown")
            result["Line Type"] = data.get("line_type", "Unknown")
        else:
            print("[!] Number invalid or not recognized.")

    except Exception as e:
        print(f"[!] Carrier check failed: {e}")

    return result
