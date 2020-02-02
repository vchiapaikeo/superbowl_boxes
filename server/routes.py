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
            'Christian',
            'Brian',
            'Ephraim',
            'Jay Ly',
            'Garrett',
            'Carmen',
            'Nina',
            'Linda',
            'Josephine',
            'Michelle',
        ]
    data = generate.gen_results(names, num_boxes).tolist()
    return jsonify(data)
