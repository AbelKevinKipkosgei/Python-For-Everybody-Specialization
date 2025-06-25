import xml.etree.ElementTree as ET

data = """
<person>
    <name>Chuck</name>
    <phone type="int">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)
print(f"Name: {tree.find('name').text}")
print(f"Attr: {tree.find('email').get('hide')}")
