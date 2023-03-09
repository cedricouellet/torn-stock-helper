from stock_lib.models import Base

class Snapshot(Base):
    '''
    A model representing a stock snapshot.
    '''
        
    __tablename__ = 'snapshot'
    
    @property
    def json(self):
        '''
        The json representation of the snapshot
        '''
        
        if self is None:
            return None
        
        return {
            'id': self.id,
            'stock_id': self.stock_id,
            'date': self.date,
            'timestamp': self.timestamp,
            'open_price': self.open_price,
            'high_price': self.high_price,
            'low_price': self.low_price,
            'close_price': self.close_price,
            'volume': self.volume,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def list_json(cls, *snapshots) -> list[dict]:
        '''
        Represent one or more snapshots into json format
        
            Paremeters:
                `snapshots`: One or more snapshots

            Returns:
                A list of json objects
        '''
                
        return [snapshot.json for snapshot in snapshots]