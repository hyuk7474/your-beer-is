from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017) # client가 robo와 같은 역할(mongodb에 연결)

db = client["your_beer_is"]
bf_data = db["bf_data"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def bf_datas_list():

    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    bf_datas = list(
        db.bf_data.find({}, {'_id': False}) # 1을 쓰면 오름차순, 아무것도 안 써도 오름차순
    )
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'bf_list': bf_datas})

    print(bf_datas)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)