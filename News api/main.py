import requests 

query = input("What news you want : ")
api_key = "3fe9fca9969942d18291a6c9718d5a40"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-03&sortBy=publishedAt&apiKey={api_key}"

print(url)
r = requests.get(url)

data = r.json()
Articles = data["articles"]

for index, Article in enumerate(Articles):
    print(index + 1, Article["title"], Article["url"])
    print("------------------------------------------------------------\n")