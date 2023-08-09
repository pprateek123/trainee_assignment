from abc import abstractmethod
class Product:
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass

def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

class discountedProduct(Product):
    def __init__(self,price,discount):
        super().__init__(price)
        self.discount = discount
    
    def calculate_price(self):
        discounted_price = self.price - (self.price * self.discount)
        return (discounted_price)


# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), Product(75)]
print("Total Price:", calculate_total_price(products))