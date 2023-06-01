

class Order():
    def __init__(self, name, price):
        self.name= name
        self.price= price
    
def GenerateOrders():
        orders=[]
        for i in range (100):
            order=Order(f"Burger{i+1}", (i+1)*10)
            orders.append(order)
        return orders    
def FindPopular(order_list):
        burger_count={}
        order_income=0

        for order in order_list:
            if order.name in burger_count:
                burger_count[order.name]+= 1
            else:
                burger_count[order.name]=1
            order_income +=order.price
        
        
        most_ordered_burger=max(burger_count ,key=burger_count.get)
        times_ordered=burger_count[most_ordered_burger]
        
        return most_ordered_burger, times_ordered , order_income     



def main():
    orders=GenerateOrders()
    popular_burger, times_ordered, total_income= FindPopular(orders)

    print(f"The times ordered: {times_ordered}")
    print(f"The most popular burger: {popular_burger}")
    print(f"The total income is: {total_income}")

main()  