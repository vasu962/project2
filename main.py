import requests as r

res = r.get("https://www.google.com/search?q=jennifer+lawrence")

print(res.text)