from pymongo import MongoClient

client = MongoClient('localhost', 27017)

#db 생성 
#nosql의 장/단점: 없으면 만들어준다
db = client.dbsparta 

# user = {
#     'name': '박지영',
#     'age': 26
# }
# db.users.insert_one(user)

# user = {
#     'name': '아무개',
#     'age': 25
# }
# db.users.insert_one(user)

#param = {'age':25}
#all_users = list(db.users.find(param))
# all_users = list(db.users.find({'age':25})) #딕셔너리로 주기때문에 리스트로 감싼다
# all_users = list(db.users.find()) 
# print(all_users)
# for user in all_users:
#     print(user['name'])

# param = {'name':'아무개'}
# all_users2 = list(db.users.find(param, {'_id': False})) #_id는 안보고 싶다

param = {'name':'아무개'}
data_to_update = {'age':30}
db.users.update_one(param, {'$set': data_to_update})