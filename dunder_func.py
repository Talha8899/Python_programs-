#dunder function creation
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    #define the dunder function
    def __gt__(self,orde2):
        return self.price>orde2.price

