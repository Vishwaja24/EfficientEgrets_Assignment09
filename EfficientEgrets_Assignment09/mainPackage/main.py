#main.py

# main.py
from RApackage.module1 import *

# Step 1: Retrieve product data
products = get_product_data()

# Step 2: Randomly select one product and store its details
product_id, description, manufacturer_id, brand_id = select_random_product(products)

# Print the details for debugging (optional)
print(f"ProductID: {product_id}, Description: {description}, ManufacturerID: {manufacturer_id}, BrandID: {brand_id}")
