from app.posts import bp
import json

@bp.route('/')
def index():
    return json.dumps([
        {'id': 1, 'title': 'Hello World', 'user': 'Cedric'},
        {'id': 2, 'title': 'Goodbye World', 'user': 'John'},
    ]) 

@bp.route('/<int:id>')
def details(id: int):
    return json.dumps({
        'id': id, 'title': 'My Title', 'user': 'Cedric'
    })
