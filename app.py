from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client["your_beer_is"]
bf_data = db["bf_data"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def bf_datas_list():

    
    bf_datas = list(
        bf_data.find({}, {'_id': False})
    )
    
    return jsonify({'result': 'success', 'bf_list': bf_datas})

    print(bf_datas)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)