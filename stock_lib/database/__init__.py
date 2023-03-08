import os
from sqlalchemy.ext.automap import automap_base as __automap_base
from sqlalchemy import create_engine as __create_engine
from sqlalchemy.engine import Engine as __engine
from sqlalchemy.orm import scoped_session as __scoped_session, sessionmaker as __sessionmaker

# Set SQLALCHEMY_URI according to env
SQLALCHEMY_URI = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ.get('DB_HOST')}:{os.environ['DB_PORT']}/{os.environ['DB_DATABASE']}"

# Create mapper 
Base = __automap_base()
    
# Members
__engine = __create_engine(SQLALCHEMY_URI)
db =  __scoped_session(__sessionmaker(autocommit=False, autoflush=False, bind=__engine))

def load_db():
    # Load models
    import stock_lib.models
    
    # Reflect tables 
    Base.prepare(autoload_with=__engine, reflect=True)
    
    # Assign session to mapper
    Base.query = db.query_property()