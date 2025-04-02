# File Name : module1.py
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


def connect_to_sql_server():
  
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    return conn

class ProductManager: 
    def __init__(self, db): 
        self.db = db 

def get_product_data():
    conn = connect_to_sql_server()
    cursor = conn.cursor()
    
    query = """
    SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID 
    FROM dbo.tProduct

    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Convert to a list of dictionaries for easier access
    products = []
    for row in results:
        products.append({
            'ProductID': row.ProductID,
            'UPC-A': row[1],  # Assuming the second column is UPC-A
            'Description': row.Description,
            'ManufacturerID': row.ManufacturerID,
            'BrandID': row.BrandID
        })
    
    cursor.close()
    conn.close()
    
    return products

# Function to randomly select one row and return relevant information
def select_random_product(products):
    selected_product = random.choice(products)
    
    product_id = selected_product['ProductID']
    description = selected_product['Description']
    manufacturer_id = selected_product['ManufacturerID']
    brand_id = selected_product['BrandID']
    
    return product_id, description, manufacturer_id, brand_id
