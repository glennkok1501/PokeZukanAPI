import os

f = open("pokemon-list.txt", 'w')
os.chdir("../images/pokemon")
ls = os.listdir()
for i in ls:
	f.write(f"{i.replace('.png','')}\n")
f.close()

print(len(ls))
