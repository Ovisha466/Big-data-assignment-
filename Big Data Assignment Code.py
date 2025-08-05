import pandas as pd
import sqlite3

def process_data():

    # Load transactions data from CSV into a pandas DataFrame
    file_path = r"src/data/transactions.csv" 
    df = pd.read_csv(file_path, encoding="utf-8")
    
    # Remove rows with missing values
    df.dropna(inplace=True)

    # Convert 'TransactionDate' to datetime format
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

    # Connect to SQLite database and create table
    conn = sqlite3.connect("src/data/transactions.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        amount REAL,
        TransactionDate TEXT,
        PaymentMethod TEXT,
        City TEXT,
        Category TEXT
    )
    """)

    # Insert the cleaned DataFrame into the database (replace existing table)
    df.to_sql("transactions", conn, if_exists="replace", index=False)

    # Query 1: Top 5 Most Sold Products
    
    cursor.execute("""
        SELECT product, COUNT(*) AS total_sold
        FROM transactions
        GROUP BY product
        ORDER BY total_sold DESC
        LIMIT 5
    """)
    print(cursor.fetchall())

    # Query 2: Monthly Revenue Trend
    
    cursor.execute("""
        SELECT strftime('%Y-%m', TransactionDate) AS month, SUM(amount) AS total_revenue
        FROM transactions
        GROUP BY month
        ORDER BY month
    """)
    print(cursor.fetchall())

    # Query 3: Payment Method Popularity
    
    cursor.execute("""
        SELECT PaymentMethod, COUNT(*) AS usage_count
        FROM transactions
        GROUP BY PaymentMethod
        ORDER BY usage_count DESC
    """)
    print(cursor.fetchall())

    # Query 4: Top 5 Cities with Most Transactions
    
    cursor.execute("""
        SELECT City, COUNT(*) AS transaction_count
        FROM transactions
        GROUP BY City
        ORDER BY transaction_count DESC
        LIMIT 5
    """)
    print(cursor.fetchall())

    # Query 5: Top 5 High-Spending Customers
    
    cursor.execute("""
        SELECT SUM(amount) AS total_spent
        FROM transactions
        ORDER BY total_spent DESC
        LIMIT 5
    """)
    print(cursor.fetchall())

    # Query 6: Hadoop vs Spark Related Product Sales
    
    cursor.execute("""
        SELECT 
            CASE 
                WHEN product LIKE '%Hadoop%' THEN 'Hadoop'
                WHEN product LIKE '%Spark%' THEN 'Spark'
                ELSE 'Other'
            END AS category,
            COUNT(*) AS total_sales
        FROM transactions
        WHERE product LIKE '%Hadoop%' OR product LIKE '%Spark%'
        GROUP BY category
    """)
    print(cursor.fetchall())

    # Query 7: Top Spending Customers in Each City
    
    cursor.execute("""
        SELECT City, MAX(total_spent) AS max_spent
        FROM (
            SELECT City, SUM(amount) AS total_spent
            FROM transactions
            GROUP BY City
        )
        GROUP BY City
    """)
    print(cursor.fetchall())

    # Close connection
    conn.commit()
    conn.close()
    print("\n✅ Data Processing & Advanced Analysis Completed Successfully!")

if __name__ == "__main__":
    process_data()
