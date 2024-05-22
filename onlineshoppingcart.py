#Online ShoppingCart
class shoppingCart():
    items_in_cart={}
    def __init__(self,customer_name):
        self.customer_name=customer_name
        
    def add_items(self,product,price):
       
        if not product in self.items_in_cart:
            self.items_in_cart[product]=price
            print(product+" Added")
        else:
            print("This product is already added")
    def remove_itmes(self,product):
        if product in  self.items_in_cart:
            del self.itmes_in_cart[product]
            print(product+" this product is removed")
        else:
            print("this product is not in cart")
    def show_items(self):
        
        return self.itmes_in_cart
my_cart=shoppingCart("My online Shoppingcart")
my_cart.add_items("rice",75)
my_cart.add_items("Sugar",45)
