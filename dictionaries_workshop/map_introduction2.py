# create a map with the following values
# 978-1-60309-452-8	A Letter to Jo
# 978-1-60309-459-7	Lupus
# 978-1-60309-444-3	Red Panda and Moon Bear
# 978-1-60309-461-0	The Lab
map={

"978-1-60309-452-8" : " A Letter to Jo",
"978-1-60309-459-7" : " Lupus",
"978-1-60309-444-3" : " Red Panda and Moon Bear",
"978-1-60309-461-0"	: " The Lab"

}
# to display key, value 
for key, value in map.items(): 
    print(value,key)

# remove the key 978-1-60309-444-3
map.pop ("978-1-60309-444-3")

# remove the key pair with the value
map.popitem()
print(map)

# Adding the following items 978-1-60309-450-4	They Called Us Enemy 
# 978-1-60309-453-5	Why Did We Trust Him?
map.update({"978-1-60309-450-4" : "They Called Us Enemy" ,
"978-1-60309-453-5": "Why Did We Trust Him?"})

# Checkingif map has 478-0-61159-424-8 as a value
print (map.get ("478-0-61159-424-8", "False"))

# Printing the value associated with 978-1-60309-453-5
print(map.get ("978-1-60309-453-5"))


