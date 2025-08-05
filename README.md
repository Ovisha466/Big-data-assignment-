# 🏆 Student Lab: Transactions Data Processing

**Project Overview**
In this project, you will work with a dataset of transactions from a business or e-commerce platform. Your task is to process the data, clean it, and then analyze it using SQL queries to derive meaningful insights about the transactions. You will be using **Python with the pandas library** for data manipulation and **SQLite** for storing and querying the data.

The project will involve the following key steps:

* **Data Cleaning**: Load the data from a CSV file, handle missing values, and convert any necessary columns (such as dates) to the correct format.
* **Database Creation and Insertion**: Create a SQLite database and insert the cleaned data into it for easy querying.
* **Advanced SQL Queries**: Write SQL queries to analyze various aspects of the data, such as the top-selling products, monthly revenue trends, and customer spending patterns.
* **Advanced Analytics**: Write complex SQL queries to explore specific business questions like identifying products with keywords (e.g., Hadoop vs. Spark) or determining cities with the highest transaction volume.

---

**Instructions**

Download the reference artifacts and open the provided files in **VS Code**.

---

**Step 1: Data Cleaning**

* **Load the Data**: Load the provided `transactions.csv` dataset into a pandas DataFrame.
* **Handle Missing Values**: Inspect the dataset for missing or null values. Remove any rows that contain missing values to ensure the data is clean and complete.
* **Convert Data Types**: Ensure the `TransactionDate` column is in proper datetime format for accurate analysis.

---

**Step 2: Create SQLite Database and Table**

* **Set Up the SQLite Database**: Use `sqlite3` to create a local SQLite database to store your transaction data.
* **Create the Table**: Create a table named `transactions` within the SQLite database with the following schema:

  ```sql
  TransactionID INTEGER PRIMARY KEY  
  CustomerID INTEGER  
  Product TEXT  
  Amount REAL  
  TransactionDate TEXT  
  PaymentMethod TEXT  
  City TEXT  
  Category TEXT
  ```

---

**Step 3: Insert Data into SQLite Database**

* **Insert Cleaned Data**: Insert the cleaned data from the pandas DataFrame into the `transactions` table in the SQLite database. If the table already contains data, replace it with the new cleaned dataset.

---

**Step 4: Perform SQL Queries for Data Analysis**

Write and execute the following SQL queries to derive insights:

* **Top 5 Best-Selling Products**: Identify the top 5 products based on the number of transactions (sales count).
* **Monthly Revenue Trend**: Calculate monthly revenue by summing the `Amount` for each month, displayed in chronological order.
* **Payment Method Popularity**: Determine the popularity of each payment method by counting the number of transactions per method.
* **Top Cities with Most Transactions**: Identify cities with the highest number of transactions.
* **Top Spending Customers**: Find the top 5 customers who have spent the most, by calculating and ordering the total amount spent per customer.
* **Compare Hadoop vs. Spark Products**: Analyze and compare sales for products associated with keywords like "Hadoop" and "Spark".
* **Top Spending Customers by City**: Use advanced SQL techniques like subqueries or ranking to identify top spenders in each city.

---

**Step 5: Execute and Verify Your Queries**

* **Execute Queries**: Run each SQL query on the database to retrieve the required data.
* **Verify Results**: Ensure the output is logical and consistent with the dataset. If any anomalies are found, review and debug your SQL logic.

---

**Step 6: Final Steps**

* **Clean Up**: After completing all tasks, close the SQLite database connection properly.
* **Commit and Close**: Commit all changes (if any) to the database and ensure the connection is properly closed to avoid data corruption.


## Instructions
1. Clone the repository to your local system.
2. Install the required VS Code extensions by running:
3. Open the project in VS Code.
4. Implement your code inside `src/main/lab.py`.
5. Run your script and check the output.
6. Commit and push your changes to GitHub.

## Notes
- The `transactions.csv` dataset is provided inside the `src/data/` folder.
- The code should read the CSV file, perform basic analysis, and store data in an SQLite database.


Good luck! 🚀
