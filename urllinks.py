import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
secure_context = ssl.create_default_context()
secure_context.check_hostname = False
secure_context.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
response = urllib.request.urlopen(url, context=secure_context)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup("span")
# print(span_tags)
span_tag_contents = []
for tag in tags:
    span_tag_contents.append(int(tag.contents[0]))

print("Sum:", sum(span_tag_contents))
