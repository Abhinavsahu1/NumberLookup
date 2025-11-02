import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import (
    NumberParseException,
    is_valid_number,
    region_code_for_number,
    is_possible_number,
)

try:
    phone_number1 = phonenumbers.parse("write your phone number here")
except NumberParseException as e:
    print("Invalid phone number:", e)
    raise SystemExit(1)

if not is_valid_number(phone_number1):
    print("Number parsed but not valid.")
    raise SystemExit(1)

print("Formatted number:", phonenumbers.format_number(phone_number1, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print("Country code:", phone_number1.country_code)
print("National number:", phone_number1.national_number)
print("Region code:", region_code_for_number(phone_number1))
print("Possible number?:", is_possible_number(phone_number1))

print("\nLocation (geocoder):", geocoder.description_for_number(phone_number1, "en") or "Unknown")
print("Carrier:", carrier.name_for_number(phone_number1, "en") or "Unknown")
print("Timezones:", ", ".join(timezone.time_zones_for_number(phone_number1)) or "Unknown")

print("\nNote: This location is approximate (country/region). You cannot get precise GPS location from a phone number alone.")