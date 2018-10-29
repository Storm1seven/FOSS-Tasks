import json, requests

def request_json():
	data = requests.get('https://pokeapi.co/api/v2/pokemon/')
	pokedex = json.loads(data.text)
	return pokedex

def get_pokemon_abilities(pokemon):
	for i in pokedex['results']:
		if i['name'] == pokemon:
			pokemon_url = i['url']
	pokemon_json = requests.get(pokemon_url)
	pokemon_data = json.loads(pokemon_json.text)
	data_return = []
	for i in pokemon_data['abilities']:
		data_return.append(i['ability']['name'])
	abilities = '\n'.join(data_return)
	print('The abilities of '+pokemon+' are:\n'+abilities)

def get_pokemon_type(pokemon):
	for i in pokedex['results']:
		if i['name'] == pokemon:
			pokemon_url = i['url']
	pokemon_json = requests.get(pokemon_url)
	pokemon_data = json.loads(pokemon_json.text)
	data_return = []
	for i in pokemon_data['types']:
		data_return.append(i['type']['name'])
	types = ', '.join(data_return)
	print(pokemon+' is of the type: '+types)

if __name__ == '__main__':
	pokedex = request_json()
	pokemon = input()
	print('Retreiving data.....')
	print('Hold on for a second..')
	get_pokemon_abilities(pokemon)
	get_pokemon_type(pokemon)