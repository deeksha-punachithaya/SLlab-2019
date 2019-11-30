myDict = {
	'name':'Deeksha',
	'usn':"1MS17IS039",
	'age':"20"
	}
	

list = ["val1","val2","val3"]
j = 0

print(myDict)

print(myDict["name"])
print(myDict.get("name"))

for i in myDict:
	print("Key is: " + i + "Value is: " + myDict[i])
	list[j] = myDict[i]
	j = j+1
	
print(list)
	
print(myDict.keys())
print(myDict.values())
print(myDict.items())
