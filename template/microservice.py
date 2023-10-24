#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})


port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)