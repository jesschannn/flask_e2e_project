import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
import pandas as pd

load_dotenv()  

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

# Path to your CSV file
csv_file_path = '/home/jessica_chan_3/flask_e2e_project/data/clean_medicalmalpractice.csv'

# Read CSV into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Create SQLAlchemy Engine
engine = create_engine(conn_string)

# Insert data into Azure SQL Database
df.to_sql('medical_malpractice', con=engine, if_exists='replace', index=False)

print("Data successfully inserted into Azure SQL Database.")

# Test
query = 'SELECT * FROM medical_malpractice'
df = pd.read_sql(query, engine)

print(df)  # Display the data