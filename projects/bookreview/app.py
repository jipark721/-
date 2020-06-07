from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta
## 여기까지 기본 세팅

# HOME HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index2.html')

# SAVE REVIEW
@app.route('/reviews', methods=['POST'])
def write_review():
    title_received = request.form['title_to_give']
    author_received = request.form['author_to_give']
    review_received = request.form['review_to_give']

    review = { #DB 저장
        'title': title_received,
        'author': author_received,
        'review': review_received
    }

    db.reviews.insert_one(review)

    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 저장되었습니다'})

# GET REVIEWS
@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': False}))
    return jsonify({'result':'success', 'reviews':reviews, 'msg': '리뷰들을 성공적으로 불러왔습니다.'})

#이게 무조건 맨아래에 있어야
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
