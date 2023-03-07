import os

# Read environment variables
__host = os.getenv('DB_HOST') 
__db_name = os.getenv('DB_DATABASE')
__username = os.getenv('DB_USER')
__password = os.getenv('DB_PASS')
__port = os.getenv('DB_PORT') 

# Set SQLALCHEMY_URI accordinly
SQLALCHEMY_URI = f'mysql+pymysql://{__username}:{__password}@{__host}:{__port}/{__db_name}'


