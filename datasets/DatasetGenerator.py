from random import randint

with open('dataSet.txt', 'w+') as dataset:
    for i in range(0, 1000):
        dataset.write(str(randint(1, 1000)) + " ")
