from sqlalchemy.ext.automap import automap_base, AutomapBase
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker

from stock_lib.database.setup import SQLALCHEMY_URI

# Create mapper 
Base = automap_base()
    
# Members
engine = create_engine(SQLALCHEMY_URI)
db =  scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def load_db():
    # Load models
    import stock_lib.models
    
    # Reflect tables 
    Base.prepare(autoload_with=engine, reflect=True)
    
    # Assign session to mapper
    Base.query = db.query_property()