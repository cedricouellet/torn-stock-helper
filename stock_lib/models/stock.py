from stock_lib.models import Base

class Stock(Base):
    '''
    A model representing a stock.
    '''
    
    __tablename__ = 'stock'

    @property
    def json(self):
        '''
        The json representation of the stock
        '''
        
        if self is None:
            return None
        
        return {
            'id': self.id,
            'name': self.name,
            'acronym': self.acronym,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    
    @classmethod
    def list_json(cls, *stocks):
        '''
        Represent one or more stocks into json format
        
            Paremeters:
                `stocks`: One or more stocks

            Returns:
                A list of json objects
        '''
                
        return [stock.json for stock in stocks]
