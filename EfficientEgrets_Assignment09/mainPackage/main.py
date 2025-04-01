#main.py

from RApackage.module1 import *  # Replace with actual module name

# Initialize database connection
db_connector = DatabaseConnector()
db_connector.connect()

# Initialize ProductManager
product_manager = ProductManager(db_connector)

# Step 1: Fetch products
product_list = product_manager.fetch_products()

# Step 2: Select a random product
if product_list:
    product_manager.select_random_product(product_list)

# Close the database connection
db_connector.close_connection()
