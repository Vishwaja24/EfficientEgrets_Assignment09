# File Name : module3.py
# Student Name: Will Claus
# email: clausws@mail.uc.edu
# Assignment Number: Assignment09
# Due Date: April 3rd, 2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: We are mixing sql and python in order to create data using our SQl instances
# Brief Description of what this module does: This module shows us how to create code in order to access our SQL Server 
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/)

# module3.py

import pyodbc
import random
from RApackage.module1 import *

def connect_to_sql_server():
    # Replace with your actual SQL Server details
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    return conn

# Function to run the query for Question 1 and return the results
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

# Function for Question 6: Fetch the total number of items sold for a specific ProductID
def get_items_sold_for_product(product_id):
    conn = connect_to_sql_server()
    cursor = conn.cursor()
    
    query = """
    SELECT TOP (100) PERCENT 
        SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail 
    INNER JOIN dbo.tTransaction 
        ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
    WHERE dbo.tTransaction.TransactionTypeID = 1 
        AND dbo.tTransactionDetail.ProductID = ?
    """
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    
    # If result is not None, return the total items sold, otherwise return 0
    number_of_items_sold = result[0] if result else 0
    
    cursor.close()
    conn.close()

    return number_of_items_sold


 



    
    
