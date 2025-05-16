info = {
    "key": "value",
    "name": "ritu",
    "college": "shipyard",
    12:34.90,
    "topics":( "dict", "set"),
    "is_adult": True,
    "marks" : [23, 44,3,1,4],

}
print(type(info))
info["sername"] = ["masha"]
print(info)
print(info["topics"])

#nested dictionary

infoMain = {
    "key": "value",
    "name": "ritu",
    "college": "shipyard",
    12:34.90,
    "topics":( "dict", "set"),
    "is_adult": True,

    "student" : {
    "marks" : [23, 44,3,1,4],
    "subject":["python","c","java"],
    "numbers": [3,55,34,24,],
},
    "mainSub":"bangla",

}
print(infoMain)
print(infoMain.keys())
print(infoMain.values())
#for covert in the type casting
print(list(infoMain.values()))
print(list(infoMain.keys()))


