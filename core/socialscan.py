
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

def check_social_links(phone_number):
    result = {
        "WhatsApp": "Unknown",
        "Telegram": "Unknown"
    }

    print("[•] Checking social media presence (this may take a few seconds)...")

    try:
        options = Options()
        options.headless = True
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")  
        options.add_argument("--silent")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        os.environ["WDM_LOG_LEVEL"] = "0"
        os.environ["PYTHONWARNINGS"] = "ignore"


        driver = webdriver.Chrome(options=options)

        # --- WhatsApp ---
        wa_url = f"https://wa.me/{phone_number.replace('+', '')}"
        driver.get(wa_url)
        time.sleep(2)
        if "Use WhatsApp" in driver.page_source or "Continue to Chat" in driver.page_source:
            result["WhatsApp"] = "Linked"
        else:
            result["WhatsApp"] = "Not Found"

        # --- Telegram ---
        tg_url = f"https://t.me/{phone_number.replace('+', '')}"
        driver.get(tg_url)
        time.sleep(2)
        if "If you have Telegram" in driver.page_source or "Preview channel" in driver.page_source:
            result["Telegram"] = "Possibly Linked"
        else:
            result["Telegram"] = "Not Found"

        driver.quit()

    except Exception as e:
        print(f"[!] Social scan error: {e}")
        result["WhatsApp"] = result["Telegram"] = "Error"

    return result
