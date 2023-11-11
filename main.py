import requests

URL = "https://www.youtube.com/watch?v=6fqgoTML93U&ab_channel=moyamawhinney"
page = requests.get(URL)

print(page.text)