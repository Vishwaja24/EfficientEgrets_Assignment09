# File Name : main.py
# Student Name: Rithu Aynampudi, Vishwaja Painjane, Will Claus
# email: aynampru@mail.uc.edu, painjavv@mail.uc.edu, clausws@mail.uc.edu
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
from WCpackage.module3 import *


# Step 1: Retrieve product data
products = get_product_data()

# Step 2: Randomly select one product and store its details
product_id, description, manufacturer_id, brand_id = select_random_product(products)

print(f"ProductID: {product_id}, Description: {description}, ManufacturerID: {manufacturer_id}, BrandID: {brand_id}")


# Step 3 & 4: Get manufacturer name
db_operations = DatabaseOperations()
manufacturer = db_operations.get_manufacturer_name(manufacturer_id)


# Step 5: Get brand name
db_operations = DatabaseOperations()

manufacturer = db_operations.get_manufacturer_name(manufacturer_id)
brand = db_operations.get_brand_name(brand_id)

print(f"Manufacturer: {manufacturer}, Brand: {brand}")


# Step 6: 
def main():
    # Get product data
    products = get_product_data()
    
    # Randomly select a product
    product_id, description, manufacturer_id, brand_id = select_random_product(products)
    
    # Get the total number of items sold for this product
    number_of_items_sold = get_items_sold_for_product(product_id)
    
    # Print the result
    print(f"Product Description: {description}")
    print(f"Manufacturer ID: {manufacturer_id}")
    print(f"Brand ID: {brand_id}")
    print(f"Total items sold for Product ID {product_id}: {number_of_items_sold}")

if __name__ == "__main__":
    main()



# Step 7: 
def main():
    # Get product data
    products = get_product_data()
    
    # Randomly select a product
    product_id, description, manufacturer_id, brand_id = select_random_product(products)
    
    # Get the total number of items sold for this product
    number_of_items_sold = get_items_sold_for_product(product_id)
    
    manufacturer_name = "Acme Corp"  
    brand_name = "SuperBrand"        
    
    # Build the grammatically correct sentence
    sentence = (f"The product '{description}' from {manufacturer_name} "
                f"and brand {brand_name} has sold {number_of_items_sold} units.")
    
    print(sentence)

if __name__ == "__main__":
    main()