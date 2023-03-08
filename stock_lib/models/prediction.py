from stock_lib.models import Base

class Prediction(Base):
    __tablename__ = 'prediction'

    @property
    def json(self):
        if self is None:
            return None
        
        return {
            'id': self.id,
            'stock_id': self.stock_id,
            'date': self.date,
            'close_price': self.close_price,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    
    @classmethod
    def list_json(cls, *predictions):
        return [prediction.json for prediction in predictions]

