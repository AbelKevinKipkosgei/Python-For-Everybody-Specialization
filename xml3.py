import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print("Retrieving", url)

opened_url = urllib.request.urlopen(url)
data = opened_url.read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
count = tree.findall(".//count")
count_numbers = []

for count_item in count:
    count_numbers.append(int(count_item.text))

print(f"Count:", len(count_numbers))
print(f"Sum:", sum(count_numbers))
