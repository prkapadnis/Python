mydict = {} #We can simply created a Empty Dictionary
print(type(mydict))
mydict = {"Pratik" : "Dadu", "Ajit" : "Bhau", "Pratiksha" : "Tau", "Nikhil" : "Golu"}
print(mydict)

#Accessing the Dictionary Key values

print(mydict["Pratik"])
print(mydict["Ajit"])
print(mydict["Pratiksha"])
print(mydict["Nikhil"])

# Modifing the Dictionary
mydict["Ajit"] = "kalya"
print(mydict)

#Nested Dictionary
mydict["Ajit"] = {"Family": "Bhau", "Friends" : "Ajit Bhau", "Best Friends" : "Kalya"}
print(mydict)
# print(mydict["Ajit"]["Family"])
# print(mydict["Ajit"]["Friends"])
# print(mydict["Ajit"]["Best Friends"])
print(mydict["Ajit"]["Family"])
names = ["Family", "Friends", "Best Friends"]
for i in names:
    for pet_name in mydict["Ajit"][i]:
        print(pet_name,end="")
    print()

# Update the Nested Dictionary
mydict["Ajit"]["Best Friends"] = "Ajya"
print(mydict)

# Dictionary Built in Functions

secondDict = mydict #If we assign a Dictionary to another variable, If we made changes in that another
secondDict["Pratik"] = "dadu"  # dictionary then it also affect the first dictionary
# print(secondDict)
# print(mydict)
#therefore use the copy() function
secondDict = mydict.copy()
secondDict["Pratik"] = "Duda"
# print(mydict)
# print(secondDict)

# print("The .items() function :", mydict.items())
# print("The get() fucntion:",mydict.get("Ajit"))
# print("The keys() function:", mydict.keys())
# print("The values() function:",mydict.values())
# print("After the update() Function:",mydict.update({"Harshal" : "Raj"}))
# print(mydict)
# print(mydict.pop("Harshal"))
# print("After the pop functions:", mydict)
# print()