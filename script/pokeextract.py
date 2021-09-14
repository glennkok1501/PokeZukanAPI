import requests
from log import log
import json
import os
from bs4 import BeautifulSoup
from log import log

url = "https://pokeapi.co/api/v2/"
pokemondb = "https://pokemondb.net/pokedex/"

def showJson(data):
	print(json.dumps(data, indent = 4))

def writeJSON(data, filepath):
	out_file = open(filepath, "w")
	json.dump(data, out_file, indent=4)
	out_file.close()

def getList():
	f = open("pokemon-list.txt", "r")
	ls = [i.strip() for i in f.readlines()]
	f.close()
	return ls

def getPercent(curr, end):
	return (f"{round((curr/end)*100,1)}%")

def pokeApiName(name):
	def splitName(form):
		i = form.split("-")
		if (len(i) <= 2):
			return form
		else:
			if form == "mr-mime-galar":
				return form
			elif "necrozma" in form:
				return f"{i[0]}-{i[1]}"
			return f"{i[0]}-{i[2]}-{i[1]}"

	if "galarian" in name:
		return splitName(name.replace("galarian", "galar"))
	elif "alolan" in name:
		return splitName(name.replace("alolan", "alola"))
	elif name == "hoopa-confined":
		return "hoopa"
	elif name == "mimikyu":
		return "mimikyu-disguised"
	elif "minior" in name:
		return name.replace("minior", "minior-red").replace("-core","")
	elif name == "gourgeist" or name == "pumpkaboo":
		return f"{name}-average"
	elif name == "morpeko-full-belly":
		return "morpeko"
	elif "necrozma" in name:
		return splitName(name)
	else:
		return name


def checkPokemonStatus():
	ls = getList()
	index = 0
	length = len(ls)
	for i in ls:
		i = pokeApiName(i)
		res = requests.get(f"{url}pokemon/{i}")
		code = res.status_code
		percent = getPercent(index,length)
		if (code != 200):
			print(f"{i} {code} - {percent}")
			log(i, "Not Found")
		else:
			pass
			print(f"{i} {code} - {percent}")
			log(i, "Found")
		index += 1

'''
This function retrieves name, id and variants from pokemondb
if the pokemon is listed. 
'''
def getBasicInfo(name, ls):
	infos = []
	res = requests.get(f"{pokemondb}{name}")
	soup = BeautifulSoup(res.text, "html.parser")
	data = soup.find("div", {"class": "sv-tabs-panel-list"}).findAll("div", {"class":"sv-tabs-panel"}, recursive=False)
	for i in range(len(data)):
		name = data[i].find("img")["src"].split("/")[-1].replace(".jpg","").replace(".png","").replace("icon-","").lower()
		if (name in ls):
			cols = data[i].find("div", {"class":"grid-row"}).findAll("div", {"class":"grid-col"}, recursive=False)
			rows = cols[1].find("table", {"class":"vitals-table"}).findAll("tr")
			for row in rows:
				header = row.find("th").text.lower()
				if "national" in header:
					_id = int(row.find("td").text)
				if "species" in header:
					species = row.find("td").text.lower()
			infos.append({
				"name": name,
				"id":_id,
				"species": species
			})
	return infos

def getAbility(obj):
	ab = obj["abilities"]
	ls = []
	for a in ab:
		values = {
			"name":"",
			"is_hidden": False
		}
		values["name"] = a["ability"]["name"]
		values["is_hidden"] = a["is_hidden"]
		ls.append(values)
	return ls

def getType(obj):
	types = obj["types"]
	ls = []
	for t in types:
		ls.append(t["type"]["name"])
	return ls

def getH_W(obj):
	h = round(0.1 * obj["height"],2) #convert dm to m
	w = round(obj["weight"] / 10,2) #convert hg to kg
	return {"height":h, "weight":w}

def getStats(obj):
	naming = {"hp":"hp",
	"attack":"attack",
	"defense":"defense",
	"special-attack":"sp. atk", 
	"special-defense":"sp. def", 
	"speed":"speed"}
	values = {
		"base_stats": {}
	}
	stats = obj["stats"]
	for s in stats:
		name = naming[s["stat"]["name"]]
		base_stat = s["base_stat"]
		values["base_stats"][name] = base_stat
	return values

def cleanName(name):
	return name.replace("-"," ")

def getArtwork(obj):
	try:
		return obj["sprites"]["other"]["official-artwork"]["front_default"]
	except Exception:
		return ""

def getEggGroup(obj):
	ls = []
	data = obj["egg_groups"]
	for d in data:
		if d["name"] == "no-eggs":
			ls.append("undiscovered")
		else:
			ls.append(d["name"])
	return ls

def getGender(obj):
	values = {
			"male":0,
			"female":0
		}
	fInt = obj["gender_rate"]
	if fInt >= 0:
		values["female"] = (fInt/8)*100
		values["male"] = 100 - values["female"]
	
	return values

def getEggCycle(obj):
	values = {
		"hatch_counter":0,
		"steps":0
	}
	values["hatch_counter"] = obj["hatch_counter"]
	values["steps"] = 255*(values["hatch_counter"]+1)
	return values

def getPokeSpecies(link):
	values = {
		"entry":"",
		"training":{
			"base_exp":0,
			"capture_rate":0,
			"growth_rate":""
		},
		"breeding":{
			"base_happiness":0,
			"egg_group":[],
			"gender":{},
			"egg_cycle":{
				
			}
		}
		
	}
	res = requests.get(link)
	obj = res.json()
	values["entry"] = getEntry(obj)
	values["training"]["capture_rate"] = obj["capture_rate"]
	values["training"]["growth_rate"] = obj["growth_rate"]["name"]
	values["breeding"]["base_happiness"] = obj["base_happiness"]
	values["breeding"]["egg_group"] = getEggGroup(obj)
	values["breeding"]["gender"].update(getGender(obj))
	values["breeding"]["egg_cycle"].update(getEggCycle(obj))
	return values

def getEntry(obj):
	entry = ""
	data = obj["flavor_text_entries"]
	for i in range(len(data)-1, -1, -1):
		if data[i]["language"]["name"] == "en":
			entry += data[i]["flavor_text"].replace("\n"," ").lower()
			break
	return entry

def getMoves(obj):
	moves = obj["moves"]
	values = {
		"moves":[]
	}
	for m in moves:
		value = {
			"name":"",
			"method":"",
			"level":0
		}
		value["name"] = m["move"]["name"]
		value["method"] = m["version_group_details"][-1]["move_learn_method"]["name"]
		value["level"] = m["version_group_details"][-1]["level_learned_at"]
		values["moves"].append(value)
	return values

def getLocation(link):
	def locVerIndex(values, ver):
		for i in range(len(values["location"])):
			if values["location"][i]["game"] == ver:
				return i
		return -1
	res = requests.get(link)
	locs = res.json()
	checked = []
	values = {
		"location":[]
	}
	for l in locs:
		game = [i["version"]["name"] for i in l["version_details"]]
		index = locVerIndex(values, game)
		if index == -1:
			value = {
				"game":[],
				"area":[]
			}
			value["game"] = game
			for m in locs:
				curGame = [i["version"]["name"] for i in m["version_details"]]
				if curGame == value["game"]:
					value["area"].append(m["location_area"]["name"])
			values["location"].append(value)

	return values



def getPokeApiInfo(basicInfo):
	values = {
		"name":cleanName(basicInfo["name"]),
		"id":basicInfo["id"],
		"info":{
			"species":basicInfo["species"],
			"abilities":[],
			"types":[],
			"height":0,
			"weight":0
		},
		"sprites":{
			"home":f"images/pokemon/{basicInfo['name']}.png",
			"artwork":""
		},
		"moves":f"data/moves/{basicInfo['name']}.json",
		"location":f"data/location/{basicInfo['name']}.json"
	}

	apiName = pokeApiName(basicInfo["name"])
	res = requests.get(f"{url}pokemon/{apiName}")
	obj = res.json()
	values["info"]["abilities"] = getAbility(obj)
	values["info"]["types"] = getType(obj)
	h_w = getH_W(obj)
	values["info"]["height"] = h_w["height"]
	values["info"]["weight"] = h_w["weight"]
	values.update(getStats(obj))
	values["sprites"]["artwork"] = getArtwork(obj)
	values.update(getPokeSpecies(obj["species"]["url"]))
	values["training"]["base_exp"] = obj["base_experience"]

	moves = getMoves(obj)
	location = getLocation(obj["location_area_encounters"])

	writeJSON(moves, f"../data/moves/{basicInfo['name']}.json")
	writeJSON(location, f"../data/location/{basicInfo['name']}.json")

	return values


def getPokemon(name):
	ls = getList()
	basicInfo = getBasicInfo(name, ls)
	for i in range(len(basicInfo)):
		data = getPokeApiInfo(basicInfo[i])
		# showJson(data)
		writeJSON(data, f"../data/pokemon/{basicInfo[i]['name']}.json")
	return basicInfo

def getAll():
	names = []
	values = {
		"count":0,
		"pokemon":[]
	}
	res = requests.get(f"{pokemondb}all")
	soup = BeautifulSoup(res.text, "html.parser")
	dex = soup.find("table", {"id": "pokedex"}).findAll("tr")

	'''compiling list to prevent dups'''
	for i in range(1, len(dex)):
		name = dex[i].find("a", {"class": "ent-name"}).get("href").split('/')[-1]
		if name not in names:
			names.append(name)


	index = 0
	checked = []
	'''extraction'''
	for i in names:
		data = getPokemon(i)

		for j in data:
			value = {
				"id":0,
				"name":"",
				"sprite":"",
				"link":""
			}
			if j["name"] not in checked:
				value["id"] = j["id"]
				value["name"] = j["name"].replace("-"," ")
				value["sprite"] = f"images/pokemon/{j['name']}.png"
				value["link"] = f"data/pokemon/{j['name']}.json"
				values["pokemon"].append(value)
				log(f"{j['name']}.json", "Success")
				print(f"{value['name']} - {getPercent(index, 1035)}")
				index += 1
				values["count"] += 1
				checked.append(j["name"])

	writeJSON(values, "../data/pokemon/all.json")
	log("all.json", "Success")


getAll()
# getPokemon("abomasnow")

def checkExtract():
	ls = getList()
	os.chdir("../data/pokemon/")
	dr = [i.replace('.json', '') for i in os.listdir()]
	diff = list(set(ls)-set(dr))
	if (len(diff) == 0):
		print("All completed")
	else:
		print(f"{diff} - Missing")
checkExtract()
