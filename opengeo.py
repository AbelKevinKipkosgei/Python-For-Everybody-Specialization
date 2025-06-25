import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/api
service_url = "https://py4e-data.dr-chuck.net/opengeo?"

# Ignore SSL certificate errors
secure_context = ssl.create_default_context()
secure_context.check_hostname = False
secure_context.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    address = address.strip()
    params = {}
    params["q"] = address

    url = service_url + urllib.parse.urlencode(params)

    print(f"Retrieving: {url}")
    with urllib.request.urlopen(url, context=secure_context) as response:
        data = response.read().decode()

        try:
            json_data = json.loads(data)
        except:
            json_data = None

        if not json_data or "features" not in json_data:
            print(f"==== Download error ====")
            print(data)
            break

        if len(json_data["features"]) == 0:
            print(f"==== Object not found ====")
            print(data)
            break

        latitude = json_data["features"][0]["properties"]["lat"]
        longitude = json_data["features"][0]["properties"]["lon"]
        location = json_data["features"][0]["properties"]["formatted"]

        print(f"Location: {location}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
