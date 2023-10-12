import requests

URI = "https://8000-xbrandonmorales-apidemo-cuatn7g96tu.ws-us105.gitpod.io"

response = requests.get(URI)

print(f"GET: {response.text}")
print(f"GET: {response.status_code}")

data = {"nombre":"Demo","email":"demo@email"}
response = requests.post(URI,json=data)

print(f"POST: {response.text}")
print(f"POST: {response.status_code}")

hfggggfbcnfmfmdjfhjfjfgnggnfbngbgn+
