from flask import Flask, render_template, jsonify, request
import json
import os

app=Flask(__name__)


@app.route("/")
def presentable():
    return render_template('pancakestart.html')

port=os.getenv('PORT') or 80

app.run(host='0.0.0.0', port=port)