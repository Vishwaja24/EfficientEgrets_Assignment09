# module3.py

import pyodbc

class Module3:
    def connect_to_database(self):
        """
        Connect to our SQL server database
        @return the connection object or None failure
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
        except:
            # What do we do if we end up here?
            # print("Unable to connect to database") # Probably not wise
            return None
        return conn

        import pyodbc

class DatabaseConnector:
    """Handles database connection and queries with a built-in connection string."""
    
    def __init__(self):
        # Connection string stored inside the class
        self.connection_string = (
            "DRIVER={SQL Server};"
            "SERVER=your_server_address;"  # Replace with your server's address
            "DATABASE=your_database_name;"  # Replace with your database's name
            "UID=your_username;"  # Replace with your username
            "PWD=your_password"  # Replace with your password
        )
        self.conn = None

    def connect(self):
        """Establishes a connection to the SQL Server."""
        try:
            self.conn = pyodbc.connect(self.connection_string)
        except Exception as e:
            print("Error connecting to database:", e)
            self.conn = None

    def execute_query(self, query, params=None):
        """Executes a SELECT query and returns results."""
        if not self.conn:
            print("Database connection not established.")
            return []
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results

    def close_connection(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

class ProductManager:
    """Handles product-related queries."""
    
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def fetch_total_sold_by_product(self, product_id):
        """Fetches total quantity sold for a given Product ID."""
        query = """
        SELECT TOP (100) PERCENT 
            SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail 
        INNER JOIN dbo.tTransaction 
            ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
        WHERE dbo.tTransaction.TransactionTypeID = 1 
            AND dbo.tTransactionDetail.ProductID = ?
        """
        
        # Execute the query with the given Product ID as a parameter
        results = self.db_connector.execute_query(query, (product_id,))
        
        if results:
            return results[0][0]  # Return the first result's 'NumberOfItemsSold'
        else:
            return 0  # No data found, return 0

# Example usage:

# Initialize the database connection
db_connector = DatabaseConnector()
db_connector.connect()

# Initialize ProductManager with the database connector
product_manager = ProductManager(db_connector)

# Example: Substitute Product ID (replace with an actual ID)
product_id = 12345  # Replace with the actual Product ID you want to query

# Fetch the total quantity sold for the given product ID
total_sold = product_manager.fetch_total_sold_by_product(product_id)

# Print the result
print(f"Total number of items sold for Product ID {product_id}: {total_sold}")

# Close the connection after use
db_connector.close_connection()
    
    
