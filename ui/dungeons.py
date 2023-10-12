import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

#print(f"GET: {response.text}"")

response_json = json.loads(response.text)

contador = 0

for resultado in response_json['response']:
    contador = contador + 1
    print(contador,  ".",resultado['name'])

#se ingresa un numero de algun personaje
numero_personaje = int(input("ingresa el numero del personaje:"))

personaje_uri = response_json['results'][numero_personaje]['uri']



