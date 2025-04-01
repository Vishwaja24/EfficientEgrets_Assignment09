# File Name : EfficientEgrets_Assignment09
# Student Name: Vishwaja Painjane
# email: painjavv@mail.uc.edu
# Assignment Number: Assignment09
# Due Date: April 3rd, 2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment creates a Python application that queries a grocery store database to display sales information about a randomly selected product.
# Brief Description of what this module does: This module retrieves the manufacturer name and brand name from the database
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/)

#module2.py

from RApackage.module1 import connect_to_sql_server

def get_manufacturer_name(manufacturer_id):
    """
    Function to get the manufacturer name using the manufacturer ID
    """
    conn = connect_to_sql_server()
    cursor = conn.cursor()
    
    query = f"""
    SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}
    """
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    manufacturer_name = result[0] if result else "Unknown Manufacturer"
    
    cursor.close()
    conn.close()
    
    return manufacturer_name

def get_brand_name(brand_id):
    """
    Function to get the brand name using the brand ID
    """
    conn = connect_to_sql_server()
    cursor = conn.cursor()
    
    query = f"""
    SELECT Brand FROM tBrand WHERE BrandID = {brand_id}
    """
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    brand_name = result[0] if result else "Unknown Brand"
    
    cursor.close()
    conn.close()
    
    return brand_name

