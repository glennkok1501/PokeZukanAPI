import requests
from log import log
import json
import os
import re

url = "https://pokeapi.co/api/v2/move/"
all_url = f"{url}?limit=844"

def showJson(data):
	print(json.dumps(data, indent = 4))

def writeJSON(data, filename):
	out_file = open(f"../moves/{filename}.json", "w")
	json.dump(data, out_file, indent=4)
	out_file.close()

def getPercent(curr, end):
	return (f"{round((curr/end)*100,1)}%")

def getEntry(ls, target):
	for i in range(len(ls)-1, -1, -1):
		if ls[i]["language"]["name"] == "en":
			return ls[i][target].replace("\n"," ").lower()

def getMove(link):
	res = requests.get(link)
	obj = res.json()

	values = {
		"name": "",
		"type": "",
		"category": "",
		"power": 0,
		"accuracy": 0,
		"pp": 0,
		"contest":"",
		"effect": "",
		"description": ""
	}

	values["name"] =  obj["name"].replace("-", " ")

	try:
		values["type"] = obj["type"]["name"]
	except:
		values["type"] = None

	try:
		values["category"] = obj["damage_class"]["name"]
	except:
		values["category"] = None

	values["power"] = obj["power"]

	values["accuracy"] = obj["accuracy"]

	values["pp"] = obj["pp"]

	try:
		values["contest"] = obj["contest_type"]["name"]
	except:
		values["contest"] = None

	try:
		values["effect"] = re.sub(r'\B\$(\w+)%', f"{obj['effect_chance']}%", getEntry(obj["effect_entries"], "short_effect"))
	except:
		values["effect"] = None
		
	try:
		values["description"] = getEntry(obj["flavor_text_entries"], "flavor_text")
	except:
		values["description"] = None

	# print(values)
	return values


def getAll():
	all_values = {
		"count":0,
		"moves":[]
	}

	res = requests.get(all_url)
	obj = res.json()["results"]

	index = 0
	limit = len(obj)
	for m in obj:
		value = {
			"name":m["name"].replace("-", " "),
			"type":"",
			"link":f"moves/{m['name']}.json"
		}

		move = getMove(m["url"])
		writeJSON(move, m["name"])

		value["type"] = move["type"]
		all_values["count"] += 1
		all_values["moves"].append(value)

		print(f"{m['name']} - {getPercent(index, limit)}")
		index += 1

	writeJSON(all_values, "all")

getAll()
# getMove(f"{url}max-guard")
