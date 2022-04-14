import requests
URL = "https://www.billboard.com/charts/hot-100/"
page = requests.get(URL)
print(page.text)
