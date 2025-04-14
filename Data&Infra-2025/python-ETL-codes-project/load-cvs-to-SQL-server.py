import pandas as pd
from sqlalchemy import create_engine

# Load CSV file into PostgreSQL database using SQLAlchemy
engine = create_engine("postgresql://user:pass@localhost:5432/mydb") # Replace with your PostgreSQL credentials
df = pd.read_csv("customer_data.csv") # Load CSV file into a DataFrame
df.to_sql("customers", engine, if_exists="replace", index=False) # Write DataFrame to PostgreSQL table
df = pd.read_sql("SELECT * FROM customers", engine) # Read data back from PostgreSQL to verify
print(df.head()) # Display the first few rows of the DataFrame

# Close the database connection
engine.dispose() # Dispose of the SQLAlchemy engine to close the connection



# Load CSV file into mysql database
# import pandas as pd
# from sqlalchemy import create_engine

# Load CSV file into MySQL database using SQLAlchemy
engine = create_engine("mysql+pymysql://user:pass@localhost:3306/mydb") # Replace with your MySQL credentials
df = pd.read_csv("customer_data.csv") # Load CSV file into a DataFrame
df.to_sql("customers", engine, if_exists="replace", index=False) # Write DataFrame to MySQL table
df = pd.read_sql("SELECT * FROM customers", engine) # Read data back from MySQL to verify
print(df.head()) # Display the first few rows of the DataFrame
