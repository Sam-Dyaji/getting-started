# Create a Sharpie class
# We should know the followings about each sharpie:
# color (which should be a string),
# width (which will be a number) and the
# inkAmount (another number)
# We need to specify the color and the width at creation
# Every sharpie is created with a default ink_amount value: 100
# We can use() the sharpie objects: using it decreases ink_amount by 10


class Sharpie():
    def __init__(self,color, width, inkAmount):
        self.color=color
        self.width= 30
        self.inkAmount= 100
    
    def use(self):
        self.inkAmount -=10

    def specify(self):
       
        print("The sharpie is",self.color ,"and", self.width,"cm wide")

sharpie=Sharpie(color="RED", width=30, inkAmount=100)

sharpie.specify()

sharpie.use()
sharpie.use()
sharpie.use()
sharpie.use()


print(sharpie.inkAmount)