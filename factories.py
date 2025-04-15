from faker import Faker
import random

fake = Faker()

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

def create_fake_product():
    name = fake.catch_phrase()  # Generates a fake product name
    price = round(random.uniform(5.0, 100.0), 2)  # Generates a price between 5 and 100
    description = fake.text(max_nb_chars=200)  # Generates a fake description
    return Product(name, price, description)

# Example usage
if __name__ == "__main__":
    fake_product = create_fake_product()
    print(f"Name: {fake_product.name}")
    print(f"Price: ${fake_product.price}")
    print(f"Description: {fake_product.description}")
 
