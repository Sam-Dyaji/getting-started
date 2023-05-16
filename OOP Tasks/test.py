# def greet (name):
#     print("Hello", name ,", how are you doing?")
#     return name





# # greet("Sam")

# def hotel_stars(stars):
#     myHotel_stars="*****"
#     return myHotel_stars

# display=hotel_stars("*****")
# print("Your hotel has ", display)

# stars="*****"
# print(stars)

# def rotateLeft(arr):
#    return arr[1:] + arr[0] if arr else []
 
# print(rotateLeft([1, 2, 3])) # should print [2, 3, 1]



# list1 = ['green', 'fox', 2015, 2020]
# list2 = [1, 2, 3, 4, 5, 6, 7]
 
# result = list1[list2[0]][list2[-1] - list2[-2]] 
# print(result)
# #because the statement"[list2[-1]- list 2[-2]]" gives a value of zero, and is multiplied with the frist statement "list1[list2[0]]"the variable "result" produces nut (zero, empty)


# def get_hottest_day(temperatures):
#     hottestDay=None
#     hottestTemperature=None


#     for temperature_dict in temperatures:
#         for day, temperature in temperature_dict.items():
#             if hottestTemperature is None or temperature > hottestTemperature:
#                 hottestDay=day
#                 hottestTemperature=temperature

#     return hottestDay
  


# temperatures = [
#    {
#        'monday': 12,
#        'wednesday': 13,
#        'friday': 14
#    },
#    {
#        'monday': 15,
#        'friday': 12
#    },
#    {
#        'tuesday': 10,
#        'thursday': 11,
#        'saturday': 12
#    },
# ]
# print(get_hottest_day(temperatures)) # should return "monday"

# class Resident:
#     def __init__(self, name):
#         self.name = name


# class Apartment:
#     def __init__(self, id, max_residents):
#         self.id = id
#         self.max_residents = max_residents
#         self.residents = []
    
#     def add(self, resident, resident.name):
#         if len(self.residents) < self.max_residents:
#             self.residents.append(resident)
#             print(f"{resident.name} has been added to {self.id}.")
#         else:
#             print(f"The flat is full.")
    
#     def remove(self, resident_name):
#         for resident in self.residents:
#             if resident.name == resident_name:
#                 self.residents.remove(resident)
#                 print(f"{resident_name} has been removed from {self.id}.")
#                 return
#         print(f"Resident {resident_name} not found in {self.id}.")
    
#     def __str__(self):
#         return f"{self.id} flat has {len(self.residents)} residents."

# class ApartmentManager:
#     def __init__(self):
#         self.apartments = []
    
#     def add(self, apartment):
#         self.apartments.append(apartment)
    
#     def remove(self, apartment_id):
#         for apartment in self.apartments:
#             if apartment.id == apartment_id:
#                 self.apartments.remove(apartment)
#                 print(f"{apartment_id} has been removed.")
#                 return
#         print(f"Apartment {apartment_id} not found.")
    
#     def get(self, apartment_id):
#         for apartment in self.apartments:
#             if apartment.id == apartment_id:
#                 return apartment
#         print(f"Apartment {apartment_id} not found.")
    
#     def __str__(self):
#         return f"ApartmentManager manages {len(self.apartments)} apartments."
    
# flat1=Apartment("FLT", 4)
# print(flat1) # should print: FLT1 flat has 3 residents.
# flat1.add('Kyle') # should print: The flat is full.
# print(flat1) # should print: FLT1 flat has 3 residents.
# flat1.remove('Jane')
# print(flat1) # should print: FLT1 flat has 2 residents.
# flat1.remove('Jane')
# print(flat1) # should print: FLT1 flat has 2 residents.

# Write a program that is capable of handling simple restaurants!
# These restaurants have only one product: menu. Different restaurants can have different prices for their menus.
# We’d like to create a new restaurant in the program by giving the name of the restaurant and the price of the menu there.
# The restaurants give a discount to their employees, they get a menu for half price, while a guest needs to pay the full price.
# The restaurants can sit customers at tables (without limitations) and can serve menus to all the current customers. 
# Whenever a menu is served, the customer pays, which is added to the income of the restaurant, 
# and the customer also stands up from the table.
# Using your solution, the following code should run without errors and print the expected results.

class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price=price
        self.customers=[]
        self.income=0

    def __str__(self):
        return f"{self.name} | {len(self.customers)} customers | menu for {self.price}$ | income: {self.income}"
    
    def sit(self, *customers):
        self.customers.extend(customers)
    
    def serve_menu(self):
        for customer in self.customers:
            if isinstance(customer, Employee):
                price = self.price / 2
            else:
                price = self.price
            print(f"{customer.name} is eating for {price}")
            self.income += price
        self.customers.clear()

class Customer:
    def __init__(self, name):
        self.name = name

class Employee(Customer):
    pass

class Guest(Customer):
    pass    

john = Employee('John')
jane = Guest('Jane')
restaurant = Restaurant('Galactica', 10)
print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 0
restaurant.sit(john, jane)
print(restaurant) # should print: Galactica | 2 customers | menu for 10$ | income: 0
restaurant.serve_menu() # should print: John is eating for 5.0\nJane is eating for 10
print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 15