from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.
## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')
## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def post_order():
    name_received = request.form['name_give']
    quantity_received = request.form['quantity_give']
    address_received = request.form['address_give']
    contact_received = request.form['contact_give']

    db.orders.insert_one({
        "name": name_received,
        "quantity": quantity_received,
        "address": address_received,
        "contact": contact_received
    })
    return jsonify({'result':'success', 'msg': '주문이 성공적으로 접수되었습니다'})

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = list(db.orders.find({}, {"_id": False}))
    return jsonify({'result':'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)