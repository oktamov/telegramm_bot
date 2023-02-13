import requests

url = "https://text-removal-ai.p.rapidapi.com/tensor"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"content-type": "multipart/form-data; boundary=---011000010111000001101001",
	"X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
	"X-RapidAPI-Host": "text-removal-ai.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
