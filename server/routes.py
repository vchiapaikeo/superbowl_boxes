from server import app, generate
from typing import List

from flask import jsonify
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
@app.route('/api')
def api(names: List[str] = None, num_boxes: int = 100) -> str:
    if not names:
        names = [
            'Victor',
            'Ephraim',
            'Jay Ly',
            'Nina',
            'Christian',
            'Ryan',
            'Jon',
            'Carmen',
            'Jay K',
            'Paulo',
            'Garrett',
            'Brian',
        ]
    data = generate.gen_results(names, num_boxes).tolist()
    return jsonify(data)
