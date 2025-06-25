import urllib.request
import json, ssl

# Ignore SSL certificate errors
secure_context = ssl.create_default_context()
secure_context.check_hostname = False
secure_context.verify_mode = ssl.CERT_NONE

while True:
    url = input(f"Enter URL: ")
    if len(url) < 1:
        break

    print(f"Retrieving URL: {url}")
    with urllib.request.urlopen(url, context=secure_context) as response:
        data = response.read().decode()

        try:
            json_data = json.loads(data)
            # print(json_data)
        except:
            json_data = None

        if not json_data or "comments" not in json_data:
            print(f"==== Download error ====")
            break

        if len(json_data["comments"]) < 1:
            print(f"==== Object not found ====")
            break

        count_list = []
        # Loop through every object to extract count
        for json_data_object in json_data["comments"]:
            count_list.append(int(json_data_object["count"]))

        print(f"Count: {len(count_list)}")
        print(f"Sum: {sum(count_list)}")
