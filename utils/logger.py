import json
import os
from colorama import Fore, Style
from datetime import datetime

def log_result(data, export_json=False):
    print(f"\n{Fore.CYAN}========== FINAL REPORT =========={Style.RESET_ALL}")
    
    for key, value in data.items():
        status_color = Fore.GREEN if "Yes" in str(value) or "Linked" in str(value) else Fore.RED
        print(f"{Fore.YELLOW}{key}:{Style.RESET_ALL} {status_color}{value}{Style.RESET_ALL}")

    if export_json:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phonerecon_result_{timestamp}.json"
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            print(f"\n{Fore.GREEN}[✔] Results saved to {filename}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to save JSON: {e}{Style.RESET_ALL}")
