import requests

url = "https://downtube.p.rapidapi.com/api/Download/authenticate"

payload = {"apiKey": ""}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
	"X-RapidAPI-Host": "downtube.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)