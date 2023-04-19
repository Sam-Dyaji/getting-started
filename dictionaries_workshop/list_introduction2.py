List_A = {"1": "Apple", "2": "Avocado", "3": "Blueberries", "4": "Durian", "5": "Lychee"

}
List_B = {"1": "Apple", "2": "Avocado", "3": "Blueberries", "4": "Durian", "5": "Lychee"

            }

# printing if durian is in List_A
for key, value in List_A.items():
    if key == "4":
        print("True")

# Removing Durian from List_B
List_B.pop ("4")
# print(List_B)

# Adding Kiwifruit to List_A
List_A.update({"5":"Kiwifruit", "6":"Lychee"})

#Comparing the length of list A and B
print(len(List_A)- len(List_B))

# Adding passion fruit and pomelo to List_B
List_B.update({"5":"Passion Fruit", "6":"Pomelo"})

# Printing out 3rd element from list_A
print(List_A.get("3"))

# Printing elemants in List_A and List_B
for key,value in List_A.items():
    print(value)
for key,value in List_B.items():
    print (value)

