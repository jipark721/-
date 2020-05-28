people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(name):
    for person in people:
        if person['name'] == name:
            return person['age']
        return '그런 사람 없습니다.'

print(get_age('bob'))
print(get_age('지영'))

# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
# def count(fruit_name):
#     count = 0
#     for fruit in fruits:
#         if fruit == fruit_name:
#             count += 1
#     return count

# print(count('사과'))
