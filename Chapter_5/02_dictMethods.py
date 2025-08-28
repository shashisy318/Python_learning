# Dictionary Methods

dict = {
    "name": "ankur",
    "class" : 12,
    "marks" : [34,56,21,89] 
}

# dict.items() : return a list of (key , value)tuples.

print(dict.items())

# dict.keys() : return a list containing dictionary keys.
# dict.values() : return a list containing dictionary values.

print(dict.keys())

# dict.update({"friends":}) : updates the dictionary with supplied key-value pairs

dict.update({"friends":"Raj"})
print(dict)

# dict.get("name") : Return value corresponding to the given key

print(dict.get("name"))

#difference btw get(key) and dict[key]

print(dict.get("name2")) # it prints none
print(dict["name2"])   # it give error

# get more methods as required from docs or chatgpt 