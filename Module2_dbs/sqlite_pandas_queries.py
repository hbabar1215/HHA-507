import pandas as pd
from sqlalchemy import create_engine

db_location = 'example.db'
engine = create_engine(f'sqlite:///{db_location}')

# read the data from the database into a pandas DataFrame
df = pd.read_sql('SELECT * FROM insertnameoftablehere', engine)

print(df.head())
