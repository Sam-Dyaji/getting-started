map ={}
# printing out the content of map
print (map.get ("89", "True"))

# Adding values
map.update({
    "97" : "a", "65" : "A", "98" : "b", "66" : "B", "99" : "c", "67" :"C"
    })

#  printing all the keys
for key,value in map.items():
     print (key)
for key,value in map.items():
     print(value)

# print(map.keys())
# print(map.values())

# Adding value D with the key 68
map.update({"68" : "D"})

#Printing how many key, value pairs are in map
print(len(map))

# printing the value associated with key 99
print (map["99"])

#Remove the key-value pair 
# with key 97 and print the associated value
remove=map.pop("97")
print (remove)

# Print whether there is an 
# associated value with key 100 or not
print(map.get("100", "False"))

# Remove all the key-value pairs
map.clear ()
# print how many key,value pairs are in map
print(len(map))

