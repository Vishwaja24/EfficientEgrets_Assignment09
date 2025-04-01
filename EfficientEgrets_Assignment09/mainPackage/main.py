# File Name : EfficientEgrets_Assignment09
# Student Name: Rithu Aynampudi, Vishwaja Painjane, Will Claus
# email: aynampru@mail.uc.edu, painjavv@mail.uc.edu
# Assignment Number: Assignment09
# Due Date: April 3rd, 2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment creates a Python application that queries a grocery store database to display sales information about a randomly selected product.
# Brief Description of what this module does: This connects to a database, retrieves product data, randomly selects one product, and obtains the associated manufacturer and brand information
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/)

#main.py

from RApackage.module1 import *
from VPpackage.module2 import *

# Step 1: Retrieve product data
products = get_product_data()

# Step 2: Randomly select one product and store its details
product_id, description, manufacturer_id, brand_id = select_random_product(products)

# Print the details for debugging (optional)
print(f"ProductID: {product_id}, Description: {description}, ManufacturerID: {manufacturer_id}, BrandID: {brand_id}")


# Step 3 & 4: Get manufacturer name
manufacturer = get_manufacturer_name(manufacturer_id)

# Step 5: Get brand name
brand = get_brand_name(brand_id)
print(f"Manufacturer: {manufacturer}, Brand: {brand}")
