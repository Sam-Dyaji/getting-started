
# products={
# "Milk" :	"1.07",
#  "Rice" :	"1.59",
#  "Eggs" :	"3.14",
#  "Cheese" :	"12.60",
#  "Chicken Breasts" :	"9.40",
#  "Apples" :	"2.31",
#  "Tomato" :	"2.58",
#  "Potato" :	"1.75",
#  "Onion"	:"1.10"
#  }

# How much does Bob pay?
# How much does Alice pay?
# Who buys more Rice?
# Who buys more Potato?
# Who buys more Ham?
# Who buys more Apples?
# Who buys more of different products?
# Who buys more items? (more pieces)

Bob={
"Milk" :	"3",
"Rice" :	"2",
"Eggs" :	"2",
"Cheese" :	"1",
"Chicken Breasts" :	"4",
"Apples" :	"1",
"Tomato" :	"2",
"Potato" :	"1"
}

Alice ={
"Rice" :	"1",
"Eggs" :	"5",
"Chicken Breasts" :	"2",
"Apples" :	"1",
"Tomato" :	"10"
}
[1.07, 1.59, 3.14, 12.60, 9.40, 2.31, 2.58, 1.75, 1.10]

# calculating cummulative of number of products and amount
Bob.update({"Milk":3.21, "Rice":3.18, "Eggs":6.28, "Cheese":12.6, 
             "Chicken Breasts": 37.6, "Apples": 2.31,"Tomato":5.16,
               "Potato":1.75 })

Alice.update({"Rice":1.59, "Eggs":15.7, "Chicken Breasts": 18.8,
                "Apples": 2.31,"Tomato":25.8 })

# How much does Bob pay
total = sum(list(Bob.values())) 
print(total)

# How much does Alice pay?
total2 = sum(list(Alice.values()))
print(total2)

# Who buys more Rice?
for key,value in Bob.items():
    #for key,value in Alice.items():
       if value==3.18:
          print ("Bob")

# Who buys more Potato?
for key,value in Bob.items():
   #for key,value in Alice.items():
    if value==1.75:
        print ("Bob")

# Who buys more Ham?
for values in Bob.items(),Alice.items():
    if values!= "Ham":
        print("no one")

# Who buys more Apples?
if Bob["Apples"]==Alice["Apples"]:
     print ("no one")

# Who buys more of different products?
if len(Bob)> len(Alice):
     print("Bob")
else:
     print("Alice")

# Who buys more items? (more pieces)
if Bob["Tomato"]< Alice["Tomato"]:
     print("Alice")
