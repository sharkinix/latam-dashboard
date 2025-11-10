# dashboard/services/country_service.py
import re
from dashboard.constants import AIRPORT_COUNTRY_MAP

def get_country_code(city_name):
    if not city_name:
        return 'xx'

    if city_name in AIRPORT_COUNTRY_MAP:
        return AIRPORT_COUNTRY_MAP[city_name]

    for key in AIRPORT_COUNTRY_MAP.keys():
        pattern = rf"\b{re.escape(key)}\b"
        if re.search(pattern, city_name, flags=re.IGNORECASE):
            return AIRPORT_COUNTRY_MAP[key]

    return 'xx'
