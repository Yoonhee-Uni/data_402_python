# import json, requests, random
#
# url = 'https://pokeapi.co/api/v2/pokemon/'
# response = requests.get(url)
# list_of_pokemon_data = json.loads(response.text)['results']
# # key_to_extract= "name"
# # list_of_pokemon_names = [pokemon[key_to_extract] for pokemon in list_of_pokemon_data]
#
# print(list_of_pokemon_data)

# cpu_pokemon_1 = list_of_pokemon_names[random.randint(0, 19)]
# cpu_pokemon_2 = list_of_pokemon_names[random.randint(0, 19)]
#
#
#
# class Pokemon :
#   def __init__(self, name,type, hitPoints, attackDamage, move):
#     self.name = name
#     self.type = type
#     self.hitPoints = hitPoints
#     self.attackDamage = attackDamage
#     self.move = move
#
import pandas as pd

data = [['a', 10],['b', 20],['c',30]]
data

df = pd.DataFrame(data, columns=['Name', 'Score'])
print(df)
