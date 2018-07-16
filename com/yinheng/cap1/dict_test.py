dict = {"name":"YINHENG", "age": 24, 2018: False}

print(dict["name"])
print(dict["age"])
print(dict[2018])

dict["name"] = "Hello"
dict["contry"] = "CHN"

print(dict["name"])
print(dict["age"])
print(dict[2018])
print(dict["contry"])

del dict["contry"]

print(dict["name"])
print(dict["age"])
print(dict[2018])

hasContry = dict.__contains__("contry")
if hasContry: print(dict["contry"])

for key in dict.keys(): print("%s-%s"%(key, dict[key]))