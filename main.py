from secrets import token_bytes
import base58

print('hello')

class Person:
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age
        self.id = base58.b58encode(token_bytes(10)).decode('utf-8')


p1 = Person('male', 25)

print(p1.id)
print(p1.sex)
print(p1.age)
