from app import app, generate
from flask import jsonify

@app.route('/')
@app.route('/api')
def api():
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
