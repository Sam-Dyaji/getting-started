# Create an Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# When creating a new animal instance these values must be set to the default 50 value
# Every animal can eat() which decreases its hunger by one
# Every animal can drink() which decreases its thirst by one
# Every animal can play() which increases both its hunger and thirst by one

class Animal:
     def __init__(self,hunger, thirsty):
         self.hunger=50
         self.thirsty=50
         
     def eat(self):
        self.hunger -=1
        

     def drink (self):
         self.thirsty-=1
         

     def play(self):
         self.hunger+=1
         self.thirsty+=1
         
dog=Animal(hunger=50, thirsty=50)

# calling the dog (method)
dog.eat()
dog.play()
dog.drink()
dog.play()
dog.drink()
dog.drink()
dog.drink()
dog.drink()

print(dog.thirsty)

