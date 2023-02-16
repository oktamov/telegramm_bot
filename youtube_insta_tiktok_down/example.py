import requests

url = "https://youtube-downloader-videos.p.rapidapi.com/"

querystring = {"url": "https://www.youtube.com/watch?v=pp1UN09Ffmo", "quality": "720"}

headers = {
    "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
    "X-RapidAPI-Host": "youtube-downloader-videos.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
