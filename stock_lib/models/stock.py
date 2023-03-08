from stock_lib.models import Base

class Stock(Base):
    __tablename__ = 'stock'

    @property
    def json(self):
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
        return [stock.json for stock in stocks]
