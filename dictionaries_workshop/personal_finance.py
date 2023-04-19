# We are going to represent our expenses 
# in a list containing integers.

# Create a list with the following items:
# 500, 1000, 1250, 175, 800 and 120
# Create an application which prints out the
#  answers to the following questions:
# How much did we spend?
# Which was our greatest expense?
# Which was our cheapest spending?
# What was the average amount of 
# # our spendings? (print this as a float value)
# The full output of your main method should be the following:

# 3845
# 1250
# 120
# 640.833

finance= {
    "1":500, "2":1000, "3": 1250, "4":175, "5":800, "6":120
}
#  How much did we spend?
total = sum(list(finance.values())) 
print(total)

# Which was our greatest expense?
max_value= max(list(finance.values()))
print(max_value)

#  Which was our cheapest spending?
min_value= min(list(finance.values()))
print(min_value)
    
# What was the average amount of 
# our spendings? (print this as a float value)
average_value= sum(list(finance.values())) / len(list(finance.values()))
print(round(average_value))