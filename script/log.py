import datetime
import os

def getTime():
	return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def createLogFile():
	if not os.path.isfile("log.csv"):
		out_file = open("log.csv", "w")
		out_file.write(f"Name,Description,Time\n")
		out_file.close()

def log(name, event):
	createLogFile()
	out_file = open("log.csv", "a")
	audit = f"{name},{event},{getTime()}"
	out_file.write(audit+"\n")
	out_file.close()
