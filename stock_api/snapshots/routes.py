from stock_api.snapshots import snapshots
from stock_lib.models import Snapshot
from stock_lib.database import db
from flask import jsonify, Response, request

@snapshots.route('/', methods = ['GET'])
def index():
    arg_stock_id = request.args.get('stock_id')
    
    query = db.query(Snapshot)
    
    if arg_stock_id is not None:
        snapshots = query.filter(Snapshot.stock_id == arg_stock_id)
    snapshots = query.all()

    return jsonify(Snapshot.list_json(*snapshots))

@snapshots.route('/<int:id>', methods = ['GET'])
def details(id: int ) -> Response:
    snapshot = db.query(Snapshot).get(id)
    if snapshot is None:
        return jsonify(None)
    
    return jsonify(snapshot.json)
