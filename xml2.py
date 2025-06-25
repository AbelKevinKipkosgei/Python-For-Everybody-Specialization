import xml.etree.ElementTree as ET

input = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff_tree = ET.fromstring(input)
stuff_user_list = stuff_tree.findall("users/user")

for user_item in stuff_user_list:
    print(f"Name: {user_item.find('name').text}")
    print(f"Id: {user_item.find('id').text}")
    print(f"Attr: {user_item.get('x')}\n")
