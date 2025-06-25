import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
secure_context = ssl.create_default_context()
secure_context.check_hostname = False
secure_context.verify_mode = ssl.CERT_NONE

# User input
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1

# Loop to follow links
for i in range(count):
    html = urllib.request.urlopen(url, context=secure_context).read()
    soup = BeautifulSoup(html, "html.parser")
    url = soup("a")[position].get("href")
    print("Retrieving", url)

# Extract last name
name = url.split("known_by_")[-1].split(".html")[0] if "known_by_" in url else "No name"
print("Extracted name:", name)
