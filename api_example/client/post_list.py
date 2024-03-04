import http.client
import json

conn = http.client.HTTPConnection("127.0.0.1", 8000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "Jolitos bandomieji" 
}

payload = ""

conn.request("GET", "/", payload, headersList)
response = conn.getresponse()
result = response.read()
data= json.loads(result)
#print(data[0]['title'])
#print(data[0])
#print(data) įvairiais būdais galima galima pasiekti norimą info


#print(result.decode("utf-8"))

for post in data:
    for key, value in post.items():
        print(f"{key}: {value}")



