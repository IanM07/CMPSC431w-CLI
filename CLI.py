import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Establish a connection to the database
db_params = {
    "dbname": "RLCS_Game_Data",
    "user": "postgres",
    "password": "password",
    "host": "localhost" 
}

def insert_data(cursor):
    table_name = input("Enter the table name where you want to insert data: ")
    columns = input("Enter the column names separated by commas: ")
    values = input("Enter the values separated by commas: ")
    query = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
        sql.Identifier(table_name),
        sql.SQL(columns),
        sql.SQL(values)
    )
    cursor.execute(query)
    print("Data inserted successfully.")

def delete_data(cursor):
    table_name = input("Enter the table name where you want to delete data: ")
    condition = input("Enter the condition for deleting data (e.g., 'column = value'): ")
    query = sql.SQL("DELETE FROM {} WHERE {};").format(
        sql.Identifier(table_name),
        sql.SQL(condition)
    )
    cursor.execute(query)
    print("Data deleted successfully.")
    
def update_data(cursor):
    table_name = input("Enter the table name where you want to update data: ")
    set_clause = input("Enter the SET clause (e.g., 'column1 = value1, column2 = value2'): ")
    condition = input("Enter the condition (e.g., 'column = value'): ")
    query = sql.SQL("UPDATE {} SET {} WHERE {};").format(
        sql.Identifier(table_name),
        sql.SQL(set_clause),
        sql.SQL(condition)
    )
    cursor.execute(query)
    print("Data updated successfully.")

def search_data(cursor):
    table_name = input("Enter the table name to search in: ")
    condition = input("Enter the condition for the search (e.g., 'column = value'): ")
    query = sql.SQL("SELECT * FROM {} WHERE {};").format(
        sql.Identifier(table_name),
        sql.SQL(condition)
    )
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Search completed.")

def aggregate_functions(cursor):
    table_name = input("Enter the table name to perform aggregate functions on: ")
    aggregate = input("Enter the aggregate function to perform (e.g., 'SUM(column_name)'): ")
    query = sql.SQL("SELECT {} FROM {};").format(
        sql.SQL(aggregate),
        sql.Identifier(table_name)
    )
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"The result of the aggregate function is: {result[0]}")

def sorting(cursor):
    table_name = input("Enter the table name to sort the data: ")
    sort_column = input("Enter the column name you want to sort by: ")
    sort_order = input("Enter the sort order (ASC/DESC): ")
    query = sql.SQL("SELECT * FROM {} ORDER BY {} {};").format(
        sql.Identifier(table_name),
        sql.Identifier(sort_column),
        sql.SQL(sort_order)
    )
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Data sorted successfully.")

def joins(cursor):
    table1 = input("Enter the first table name for the join: ")
    table2 = input("Enter the second table name for the join: ")
    table1_key = input("Enter the join key from the first table: ")
    table2_key = input("Enter the join key from the second table: ")
    query = sql.SQL("SELECT * FROM {} INNER JOIN {} ON {}.{} = {}.{};").format(
        sql.Identifier(table1),
        sql.Identifier(table2),
        sql.Identifier(table1),
        sql.Identifier(table1_key),
        sql.Identifier(table2),
        sql.Identifier(table2_key)
    )
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Join operation completed successfully.")

def grouping(cursor):
    table_name = input("Enter the table name to perform grouping: ")
    group_column = input("Enter the column name you want to group by: ")
    aggregate = input("Enter the aggregate function for the group (e.g., 'COUNT(*)'): ")
    query = sql.SQL("SELECT {}, {} FROM {} GROUP BY {};").format(
        sql.Identifier(group_column),
        sql.SQL(aggregate),
        sql.Identifier(table_name),
        sql.Identifier(group_column)
    )
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Grouping operation completed successfully.")

def subqueries(cursor):
    table_name = input("Enter the table name where you want to perform a subquery: ")
    column_name = input("Enter the column name for the subquery condition: ")
    subquery = input("Enter the subquery (e.g., 'SELECT column FROM table WHERE condition'): ")
    query = sql.SQL("SELECT * FROM {} WHERE {} IN ({});").format(
        sql.Identifier(table_name),
        sql.Identifier(column_name),
        sql.SQL(subquery)
    )
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("Subquery operation completed successfully.")

def main():
    options = {
        "1": insert_data,
        "2": delete_data,
        "3": update_data,
        "4": search_data,
        "5": aggregate_functions,
        "6": sorting,
        "7": joins,
        "8": grouping,
        "9": subqueries
    }
    
    # Handles transaction management
    conn = psycopg2.connect(**db_params)
    conn.set_session(autocommit=False)
    cursor = conn.cursor()

    while True:
        print("\nWelcome to the Database CLI Interface!")
        print("Please select an option:")
        print("1. Insert Data")
        print("2. Delete Data")
        print("3. Update Data")
        print("4. Search Data")
        print("5. Aggregate Functions")
        print("6. Sorting")
        print("7. Joins")
        print("8. Grouping")
        print("9. Subqueries")
        print("10. Exit")

        choice = input("\nEnter your choice (1-10): ")

        try:
            if choice in options:
                options[choice](cursor)
                conn.commit()
                print("Transaction committed.")
            elif choice == "10":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            conn.rollback()
            print(f"An error occurred: {e}. Transaction rolled back.")

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

# Close the cursor and connection
cursor.close()
conn.close()
