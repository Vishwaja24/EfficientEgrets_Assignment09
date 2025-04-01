# File Name : EfficientEgrets_Assignment09
# Student Name: Rithu Aynampudi
# email: aynampru@mail.uc.edu
# Assignment Number: Assignment09
# Due Date: April 3rd, 2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are mixing sql and python in order to create data using our SQl instances
# Brief Description of what this module does: This module shows us how to create code in order to access our SQL Server 
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/)

#module1.py 
import pyodbc
import random

class DatabaseConnector:
    """Handles database connection and queries with a built-in connection string."""
    
    def __init__(self):
        # Connection string stored inside the class
        self.connection_string = (
            "DRIVER={SQL Server};"
            "SERVER=your_server_address;"
            "DATABASE=your_database_name;"
            "UID=your_username;"
            "PWD=your_password"
        )
        self.conn = None

    def connect(self):
        """Establishes a connection to the SQL Server."""
        try:
            self.conn = pyodbc.connect(self.connection_string)
        except Exception as e:
            print("Error connecting to database:", e)
            self.conn = None

    def execute_query(self, query):
        """Executes a SELECT query and returns results."""
        if not self.conn:
            print("Database connection not established.")
            return []
        
        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def close_connection(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

class ProductManager:
    """Handles fetching and selecting a random product."""
    
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def fetch_products(self):
        """Fetches all products from the tProduct table."""
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        results = self.db_connector.execute_query(query)
        
        products = [
            {
                "ProductID": row[0],
                "Description": row[2],  
                "ManufacturerID": row[3],
                "BrandID": row[4]
            }
            for row in results
        ]
        return products

    def select_random_product(self, products):
        """Randomly selects one product from the list and prints details."""
        if not products:
            print("No products found.")
            return None

        selected_product = random.choice(products)

        product_id = selected_product["ProductID"]
        description = selected_product["Description"]
        manufacturer_id = selected_product["ManufacturerID"]
        brand_id = selected_product["BrandID"]

        print("\nRandomly Selected Product:")
        print(f"Product ID: {product_id}")
        print(f"Description: {description}")
        print(f"Manufacturer ID: {manufacturer_id}")
        print(f"Brand ID: {brand_id}")

        return product_id, description, manufacturer_id, brand_id


