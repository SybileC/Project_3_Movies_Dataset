from flask import Flask, jsonify, render_template
#from api.data import data_connector

from flask import request

app = Flask(__name__, static_url_path='')


# serve a dynamic html file from the flask app
@app.route('/')
def index():
    return render_template('html/index.html')


@app.route('/get_info', methods=['POST'])
def get_info():

    return(request.form['feedback'])


# serve data from the flask app
#@app.route('/data1')
#def data1():
#    return jsonify(data_connector.get_data1())
