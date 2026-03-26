# dict={"brand":"ford","model":"mustang","year":1964}

# print(dict)
# print("")
# print(dict["brand"])

dict={"brand":"ford","model":"mustang","year":1964,"year":2024}
# print(dict)
# print("length of dict",len(dict))
# print(type(dict))


# #  dict() constructor 

# dict1=dict(name="vishnu",age=22,sex="m")
# print(dict1)

# # accessiing the items 
# dict={"brand":"ford","model":"mustang","year":1964}

# print(dict["brand"])
# print(dict["model"])

# # #get()method

# print(dict.get("year"))

# # keys() method 
# print(dict.keys())  #dict_keys(['brand', 'model', 'year'])

# # # to add keys after creation 
# dict["color"]="black"  #{'brand': 'ford', 'model': 'mustang', 'year': 1964, 'color': 'black'}

# # print(dict)   

# # The values() method will return a list of all the values in the dictionary.
# print(dict.values())
# dict["colour"]="red"

# print(dict)

# The items() method will return each item in a dictionary, as tuples in a list.

# print(dict.items())


# Change Values
# # You can change the value of a specific item by referring to its key name:
# dict["year"]=2026
# print(dict)


# update method in dicit[ Update the "year" of the car by using the update() method:]

# dict.update({"year":2003})
# print("updated dic ",dict)

# removing items 
#pop()
# dict.pop("model")
# print(dict)     #{'brand': 'ford', 'year': 1964}


#popitem() removes the last inserted item from the dicitonary 
# dict["clour"]="red"
# # print(dict)
# dict.popitem()
# print(dict) 

# del keyword is used to item from dicitonary and also delete the dictionary 
# del dict["brand"]
# print(dict)

# del dict
# print(dict)

# dict.clear()
# print(dict)


# d3={1:["one","two"],2:"three"}
# print(d3)
d={}
print(type(d))
d3=dict([(1,["one","two","three"]),(2,"hello"),(2,["hello","hii"])])
print(d3)

# d=dict()
# print(type(d))
# # d=dict((1,["one","two"]),("2","three"))
# # print(d)

dict1={"name":"vishnu","age":23,"gender":"m"}
print(dict | dict1)




