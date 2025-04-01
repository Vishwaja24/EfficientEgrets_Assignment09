#module1.py 

import pyodbc
import random

# Database connection details (Update these with your actual credentials)
SERVER = "your_server_address"
DATABASE = "your_database_name"
USERNAME = "your_username"
PASSWORD = "your_password"
DRIVER = "{SQL Server}"  # Use "{ODBC Driver 17 for SQL Server}" if needed

def connect_to_db():
    """Establish connection to SQL Server using pyodbc."""
    try:
        conn = pyodbc.connect(
            f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def fetch_products():
    """Fetch all products from tProduct table."""
    query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
    
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        
        # Convert results into a list of dictionaries
        products = [
            {
                "ProductID": row[0],
                "Description": row[2],  # Adjust based on column order
                "ManufacturerID": row[3],
                "BrandID": row[4]
            }
            for row in results
        ]
        return products
    return []

def select_random_product(products):
    """Randomly select one product and store values in variables."""
    if not products:
        print("No products found.")
        return None

    selected_product = random.choice(products)

    # Storing values in variables
    product_id = selected_product["ProductID"]
    description = selected_product["Description"]
    manufacturer_id = selected_product["ManufacturerID"]
    brand_id = selected_product["BrandID"]

    # Print values to verify
    print(f"Selected Product: {description} (ID: {product_id})")
    print(f"Manufacturer ID: {manufacturer_id}, Brand ID: {brand_id}")

    return product_id, description, manufacturer_id, brand_id

# Execute Steps 1 & 2
product_list = fetch_products()
if product_list:
    product_id, description, manufacturer_id, brand_id = select_random_product(product_list)

