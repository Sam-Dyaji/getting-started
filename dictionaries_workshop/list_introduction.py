
names = {
    
        }

# printing zero
print(len(names))

# printing false value
print (names.get ("1.", "False"))


# Adding William to the list
names.update({ "1." : "William" })

# Adding John to the list 
names.update({"2." : "John"})

# Adding Amanda to the list 
names.update({"3." : "Amanda"})

# printing number of elemnts in the list
print(len(names))

#printing out value for Amanda
print(names["3."])

#printing out value for William
print(names["1."])

#printing out value for John
print(names["2."])

# printing the value for Amanda
print(names.get("3."))

# printing keys and values 
for key,value in names.items():
    print (key, value)
#printing in reverse 
names.__reversed__
print(value)

# printing reversed value
print (names["1."])

names.clear()
print (len(names))
