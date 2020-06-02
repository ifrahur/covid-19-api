from flask import Flask, request, jsonify
from countires import getData
from india2 import getIndiaData
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "bored_bro"
CORS(app)


@app.route('/')
def home():
    return 'Covid-19 API is UP and running!<br><br>Made by <a href="https://ifrahur.me/">Ifrahur Rahman</a> add <a href= "/country"> /country</a>  for country data and  <a href= "/india"> /india</a> for indian state data'


@app.route('/country')
def country():
    if request.method == 'GET':
        return jsonify(getData())


@app.route('/india')
def india():
    if request.method == 'GET':
        return jsonify(getIndiaData())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
