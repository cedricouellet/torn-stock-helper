from stock_lib.models import Base

class Prediction(Base):
    '''
    A model representing a stock prediction.
    '''

    __tablename__ = 'prediction'

    @property
    def json(self): 
        '''
        The json representation of the prediction
        '''
        
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
    def list_json(cls, *predictions) -> list[dict]:
        '''
        Represent one or more predictions into json format
        
            Paremeters:
                `predictions`: One or more predictions

            Returns:
                A list of json objects
        '''

        return [prediction.json for prediction in predictions]

