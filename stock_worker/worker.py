#!/usr/bin/env python3

'''
Main script for the stock worker
'''

from datetime import datetime
import os
import sys


def main():
    print(f'Running worker at {datetime.now()}')
    from stock_lib.database import load_db, db
    from stock_lib.models import Stock
    from stock_lib.torn_api import TornApi

    load_db()

    api_key = os.environ['TORN_API_KEY']

    api = TornApi(api_key)
    
    response = api.get('/torn',{'selections': 'stocks'})
    data: dict = response.json()['stocks']
    stock_ids = data.keys()

    for id in stock_ids:
        # /torn/id?selections=stocks
        # if not in DB, add to db
        # add snapshot        
        pass

if __name__ == '__main__':
    main()