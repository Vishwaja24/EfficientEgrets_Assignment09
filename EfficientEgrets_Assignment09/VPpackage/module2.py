# File Name : module2.py
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


class DatabaseOperations:
    def __init__(self):
        self.conn = connect_to_sql_server()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_manufacturer_name(self, manufacturer_id):
        """
        Method to get the manufacturer name using the manufacturer ID
        """
        query = f"""
        SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}
        """
        
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        return result[0] if result else "Unknown Manufacturer"

    def get_brand_name(self, brand_id):
        """
        Method to get the brand name using the brand ID
        """
        query = f"""
        SELECT Brand FROM tBrand WHERE BrandID = {brand_id}
        """
        
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        return result[0] if result else "Unknown Brand"


