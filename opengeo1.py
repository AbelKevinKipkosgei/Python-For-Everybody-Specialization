import urllib.request, urllib.parse
import json, ssl

# No rate API
service_url = "https://py4e-data.dr-chuck.net/opengeo?"

# Ignore SSL certificate errors
secure_context = ssl.create_default_context()
secure_context.check_hostname = False
secure_context.verify_mode = ssl.CERT_NONE

while True:
    address = input(f"Enter location: ").strip()
    params = {}
    params["q"] = address

    if len(address) < 1:
        break

    # Generate full url
    url = service_url + urllib.parse.urlencode(params)
    print(f"Retrieving {url}")

    # Open URL and parse data
    with urllib.request.urlopen(url, context=secure_context) as response:
        data = response.read().decode()

        try:
            json_data = json.loads(data)
        except:
            json_data = None

        if not json_data or "features" not in json_data:
            print(f"==== Download error ====")
            break

        if len(json_data["features"]) < 1:
            print(f"==== Object not found ====")
            break

        plus_code = json_data["features"][0]["properties"]["plus_code"]
        print(f"Plus code {plus_code}")
