from core.geolocate import get_geolocation
from core.carrier_check import get_carrier_info
from core.socialscan import check_social_links
from core.scamchecker import check_scam_reports
from utils.banner import show_banner
from utils.logger import log_result

import argparse


def main():
    show_banner()
    parser = argparse.ArgumentParser(description="PhoneRecon - Phone Number OSINT Tool")
    parser.add_argument("phone", help="Phone number in international format, e.g., +639123456789")
    parser.add_argument("--json", action="store_true", help="Export results as JSON")
    args = parser.parse_args()

    phone_number = args.phone
    result = {}

    print("[•] Analyzing number:", phone_number)

    result.update(get_geolocation(phone_number))
    result.update(get_carrier_info(phone_number))
    result.update(check_social_links(phone_number))
    result.update(check_scam_reports(phone_number))

    log_result(result, export_json=args.json)


if __name__ == "__main__":
    main()
