info = {
    "key": "value",
    "name": "ritu",
    "college": "shipyard",
    12: 34.90,
    "topics": ("dict", "set"),
    "is_adult": True,
    "marks": [23, 44, 3, 1, 4],

}
print(type(info))
info["sername"] = ["masha"]
print(info)
print(info["topics"])

# nested dictionary

infoMain = {
    "key": "value",
    "name": "ritu",
    "college": "shipyard",
    12: 34.90,
    "topics": ("dict", "set"),
    "is_adult": True,

    "student": {
        "marks": [23, 44, 3, 1, 4],
        "subject": ["python", "c", "java"],
        "numbers": [3, 55, 34, 24, ],
    },
    "mainSub": "bangla",

}
print(infoMain)
print(infoMain.keys())
print(infoMain.values())
# for covert in the type casting
print(list(infoMain.values()))
print(list(infoMain.keys()))
print((infoMain.get("mainSub")))

# for update opeartion

newDict = {
    "name": "marishs",
    "age": 34,
    "class": 4,
}
infoMain.update(newDict)
print(infoMain)

# set in python
collection = {2, 3, 3, 323, 34, "hello", "hello", "world"}
collection2 = {23, 44, 3, 23, 22, 34, 3}
# duolicate value print only once
print(collection)
print(type(collection))
print(collection.pop())
print(collection)
print(collection.pop())
# randmply element gulo pop hobe
print(collection)

# union and intersection

print(collection.intersection(collection2))
print(collection.union(collection2))
# just duolicate gulo akbar kore print hobe
languages = {
    "Python",
    "Bash",
    "Python",
    "Bash",
    "PowerShell",
    "Perl",
}
print(len(languages))

#this is the dictionary example
marks={}

x=int(input("enter phy :"))
marks.update({"phy": x})

x=int(input("enter math :"))
marks.update({"math": x})

x=int(input("enter ban :"))
marks.update({"ban": x})
print(marks)
# set is always defined by {}


