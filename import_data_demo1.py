import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the path to the CSV file
csv_file_path = 'demo3_output.csv'

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
except FileNotFoundError as e:
    logging.error(f"File not found: {csv_file_path}")
    raise e
except pd.errors.EmptyDataError as e:
    logging.error(f"No data: {csv_file_path} is empty")
    raise e
except pd.errors.ParserError as e:
    logging.error(f"Parsing error: Could not parse {csv_file_path}")
    raise e
except Exception as e:
    logging.error(f"Unexpected error reading {csv_file_path}: {e}")
    raise e

# Define the database connection parameters
db_type = 'mysql'  # or 'postgresql', 'sqlite', etc.
db_driver = 'pymysql'  # or appropriate driver for your database
db_user = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_name = 'your_database'
table_name = 'your_table_name'

# Create the database connection URL
database_url = f'{db_type}+{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

try:
    # Create a SQLAlchemy engine
    engine = create_engine(database_url)

    # Insert the data into the SQL database
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    logging.info(f"Data from '{csv_file_path}' has been imported into the '{table_name}' table in the '{db_name}' database.")
except SQLAlchemyError as e:
    logging.error(f"SQLAlchemy error: {e}")
except Exception as e:
    logging.error(f"Unexpected error inserting data into database: {e}")

# Individual row processing in case of row-level errors
for index, row in df.iterrows():
    try:
        row_df = pd.DataFrame([row])
        row_df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    except SQLAlchemyError as e:
        logging.error(f"SQLAlchemy error on row {index}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error on row {index}: {e}")
