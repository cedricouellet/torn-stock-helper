#!/usr/bin/env python3

'''
Main script for the stock worker
'''

import os
from datetime import datetime

from stock_lib.database import load_db, db
from stock_lib.models import Stock, Snapshot
from stock_lib.torn_api_client import TornApiClient

def log(message: str, error=False):
    '''
    Logs a message to the console.

        Parameters:
            `message`: The message to log
            `error`: Whether or not the log level is error
    '''
    status = "ERROR" if error else "INFO"
    date = datetime.now()
    print(f'[{date}] {status}: {message}')


def main():
    '''
    `worker.py` entrypoint method. 
    '''
    log(f'Running worker')
    
    load_db()
    log('database loaded')

    api_key= os.environ['TORN_API_KEY']

    api = TornApiClient(api_key)
    
    # stock list response format: 
    # { "stocks": { "1": { ... }, "2": { ... }, (etc) } }
    stocks_response =  api.get('/torn',{'selections': 'stocks'})
    log('fetched stock list from Torn API')
    # get "stocks" node
    stocks_json: dict = stocks_response.json()['stocks']
    
    # select keys, which represent Torn stock ids
    stock_ids = stocks_json.keys()

    for id in stock_ids:
        # stock details response format:
        # { "stocks": { "1": { ... } } }
        stock_response = api.get(f'/torn/{id}', {'selections': 'stocks'})
        stock_json: dict = stock_response.json()['stocks'][id]
        log(f'fetched stock details for torn stock id: {id}')

        # get existing stock with unique torn id
        stock = db.query(Stock).filter(Stock.torn_id == id).one_or_none() 

        # if does not exist, add it to db
        if stock is None:
            stock = Stock(
                torn_id=int(id),
                name=stock_json['name'],
                acronym=stock_json['acronym']
            )
            db.add(stock)
            db.commit()
            log(f'added new db record for torn stock id: {id}')
        else:
            log(f'found db record for torn stock id: {id}')

        # create snapshot
        curr_date = datetime.utcnow()
        last_hour_json = stock_json['last_hour']
        db.add(Snapshot(
            stock_id=stock.id,
            date=curr_date,
            timestamp=int(curr_date.timestamp()),
            volume=stock_json['total_shares'],
            open_price=last_hour_json['start'],
            high_price=last_hour_json['high'],
            low_price=last_hour_json['low'],
            close_price=last_hour_json['end']
        ))

        # commit transaction
        db.commit()
        log(f'created snapshot for torn stock id: {id}')

    # close db connection
    db.close()
    log(f'task complete, db connection closed')


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        log(str(e), error=True)
        try:
            db.close()
        except:
            pass