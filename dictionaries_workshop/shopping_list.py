# We are going to represent a shopping list by a list containing strings.

# Create a list with the following items:
# eggs, milk, fish, apples, bread and chicken
# Create an application which prints out the answers to the following questions:
# Do we have milk in the shopping list? (yes/no)
# Do we have bananas in the shopping list? (yes/no)
# The full output of your main method should be the following:

# yes
# no

groceries={"1":"eggs",
            "2":"milk",
              "3":"fish",
                "4":"apples",
                  "5":"bread",
                    "6":"chicken"
        
    }

# Do we have milk in the shopping list? 
for key,value in groceries.items():
    if value == "milk":
        print("yes")
        # else:
    #     print("no")

# Do we have bananas in the shopping list?
print(groceries.get("bananas","no"))