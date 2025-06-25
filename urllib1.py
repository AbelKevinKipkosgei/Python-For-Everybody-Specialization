import urllib.request, urllib.error

try:
    url = "http://data.pr4e.org/romeo.txt"
    with urllib.request.urlopen(url) as file_handle:
        for line in file_handle:
            print(line.decode().strip())
except urllib.error.URLError as e:
    print(f"Failed to fetch URL: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
