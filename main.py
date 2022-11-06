class Restaurant():
    """Простая модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

my_rest = Restaurant("MD","trash")
my_rest.open_restaurant()
my_rest.describe_restaurant()
yir_rest = Restaurant('test','test2'
)