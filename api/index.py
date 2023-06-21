from flask import Flask, render_template, jsonify
from lib.common import get_counts

app = Flask(__name__)
counts = get_counts()


@app.route('/')
def home():
    if (counts != None):
        return render_template('index.html', countdown_data=counts['Countdowns'])
    else:
        return render_template('error.html'), 500

@app.route('/api/countdowns')
def countdowns_raw():
    if (counts == None):
        return jsonify({'error': 'Data Unavailable'}), 500
    else:
        return jsonify(counts)
