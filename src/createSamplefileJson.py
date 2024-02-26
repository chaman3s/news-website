import urllib.request, json 
with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=bf091f1660e04e1fbac2f5b565df69a0&page=1&pageSize=38") as url:
    data = json.load(url)
    print(data)