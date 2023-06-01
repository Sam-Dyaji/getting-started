class Product():
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount
    
    def GetDiscount(self):
        old_price=self.price
        new_price=self.price* (1- self.discount/100)

        return self.name, old_price, new_price

def main():
    product=Product("Rice",12000.0,20)

    name, old_price, new_price=product.GetDiscount()

    print ("Product: ", name)
    print("Old Price: ", old_price)
    print("New Price: ", new_price)

if __name__ =='__main__':
    main()


