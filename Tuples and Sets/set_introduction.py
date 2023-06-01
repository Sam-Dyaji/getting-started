Student=set()
# Set created

Student.add("Samuel")
Student.add(30)
Student.add(1.78)
Student.add("Kaduna")
Student.add(100)
# Variables added to the set

print(len(Student)) #Checking the length of the set

#Removing 2 items from the set
Student.remove(30)
Student.discard("Kaduna")

print(len(Student)) #Checking the length of the set

# Iterate over the set and print its members

print(Student)
# Remove 482 from the set if it is present

# Student.remove(482)

# Remove 42 from the set even if it is not present
Student.discard(42)