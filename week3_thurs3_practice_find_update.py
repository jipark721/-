from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

criteria = {'title': '매트릭스'}
target_movie = db.movies.find_one(criteria)
target_rating = target_movie['rating']
print(target_rating)

criteria2 = {'rating': target_rating}
same_rating_movies = list(db.movies.find(criteria2))
print(same_rating_movies)
for movie in same_rating_movies:
    print(movie['title'])

set_data = {'rating': 0}
db.movies.update_many(criteria2, {'$set': set_data})


