import requests
from log import log
import json

url = "https://pokeapi.co/api/v2/ability/"
all_url = f"{url}?limit=327"

def showJson(data):
	print(json.dumps(data, indent = 4))

def writeJSON(data, filename):
	out_file = open(f"../abilities/{filename}.json", "w")
	json.dump(data, out_file, indent=4)
	out_file.close()

def getPercent(curr, end):
	return (f"{round((curr/end)*100,1)}%")

def getEntry(ls, target):
	for i in range(len(ls)-1, -1, -1):
		if ls[i]["language"]["name"] == "en":
			return ls[i][target].replace("\n"," ").lower()

def getAbility(link):

	values = {
		"name":"",
		"effect":"",
		"description":""
	}

	res = requests.get(link)
	obj = res.json()
	values["name"] = obj["name"].replace("-", " ")
	values["effect"] = getEntry(obj["effect_entries"], "effect")
	values["description"] = getEntry(obj["flavor_text_entries"], "flavor_text")

	return values

def getAll():

	all_values = {
		"count":0,
		"abilities":[]
	}


	res = requests.get(all_url)
	obj = res.json()["results"]
	index = 0
	limit = len(obj)
	for a in obj:
		value = {
			"name":a["name"].replace("-", " "),
			"link":f"abilities/{a['name']}.json"
		}

		ability = getAbility(a["url"])
		writeJSON(ability, a["name"])

		all_values["count"] += 1
		all_values["abilities"].append(value)

		print(f"{a['name']} - {getPercent(index, limit)}")
		index += 1

	writeJSON(all_values, "all")

# getAbility(f"{url}lightning-rod")
getAll()