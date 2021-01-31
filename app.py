from flask import Flask, jsonify, render_template
#from api.data import data_connector

app = Flask(__name__, static_url_path='')


# serve a dynamic html file from the flask app
@app.route('/')
def index():
    return render_template('html/index.html')


# serve data from the flask app
#@app.route('/data1')
#def data1():
#    return jsonify(data_connector.get_data1())
