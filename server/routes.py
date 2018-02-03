from server import app, generate
from flask import jsonify
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@app.route('/api')
def api() -> str:
    data = generate.gen_results([
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
        ], 100).tolist()
    return jsonify(data)
