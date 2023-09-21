import pandas as pd

from sqlalchemy import create_engine
# Replace these values with your actual database information
hostname = "gator3228.hostgator.com"
username = "rbrennan_sm_bcd"
password = "This_is_not_the_password"
database = "rbrennan_stock_project_4"
# Create a database connection
db_url = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{database}"
engine = create_engine(db_url)
# Test the connection
try:
    conn = engine.connect()
    print("Connected to MySQL database")
except Exception as e:
    print("Error:", e)
data = pd.read_sql("SELECT * FROM Amazon", conn)
data.head()