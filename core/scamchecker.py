import requests

def check_scam_reports(phone_number):
    result = {
        "Fraud Score": "Unknown",
        "Reported as Scam": "Unknown",
        "Spammer": "Unknown",
        "VOIP": "Unknown"
    }

    try:
        print("[•] Checking for scam/fraud reports...")
        API_KEY = "RjpsWitHSPsJX0ECKp3sdNLEaMkn4JI2" 
        url = f"https://ipqualityscore.com/api/json/phone/{API_KEY}/{phone_number}"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("valid") is True:
            result["Fraud Score"] = data.get("fraud_score", "Unknown")
            result["Reported as Scam"] = "Yes" if data.get("recent_abuse") else "No"
            result["Spammer"] = "Yes" if data.get("spammer") else "No"
            result["VOIP"] = "Yes" if data.get("VOIP") else "No"
        else:
            print("[!] Could not validate phone number or fetch scam data.")

    except Exception as e:
        print(f"[!] Scam check failed: {e}")

    return result

