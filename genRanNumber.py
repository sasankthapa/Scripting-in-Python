#generate a random number of a specific length

import random
list=range(0,10)

def createNumber(length):
    num=""
    for i in range(0,length):
        num=num+str(random.choice(list))
    return num

print(createNumber(10))
print(createNumber(3))
print(createNumber(6))
