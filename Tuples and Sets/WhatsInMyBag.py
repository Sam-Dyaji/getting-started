# Instantiating Oliver and Ethan sets without assigned values
Oliver=set()
Ethan=set()

# Instantiating mia set and assigning variables to it
Mia=set(["Laptop", "Sunglasses", "Hand Sanitizer"])

# Adding items to Oliver's bag
Oliver.add("Laptop")
Oliver.add("Notebook")
Oliver.add("Pen")
Oliver.add("Sunglasses")
Oliver.add("Hand Sanitizer")

# Adding items to Ethan's bag
Ethan.add("Sunglasses")
Ethan.add("Notebook")
Ethan.add("Phone")

print(len(Oliver))
print(len(Ethan))
print(len(Mia))

# What are the common items in Oliver's and Ethan's bag?
print("The items in Oliver's bag and Ethan's are: ", Oliver.intersection(Ethan))

# What are the items that in Oliver's bag but not in Mia's bag? 
print ("The items that are in Oliver's bag but not in Mia's are: ",Oliver.difference(Mia))

# What are the common items in Oliver's, Ethan's and Mia's bag?
Oliver.intersection(Mia)
Oliver.intersection_update(Ethan)

print("The common items in Oliver's, Ethan's and Mia's bags are:",Oliver.intersection(Mia))