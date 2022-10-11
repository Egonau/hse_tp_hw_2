import random


def generate_time():
    for i in range(1, 100):
        f = open("tests/test_{}".format(i), "w+")
        strr = "1"
        for j in range(0, 10000 * (1 + i)):
            a = random.randint(1, 1000)
            strr += (" " + str(a))
        f.write(strr)
        print(i)


def generate_big():
    f = open("tests/test_duration", "w+")
    strr = "1"
    for j in range(0, 100000):
        a = random.randint(1, 1000)
        strr += (" " + str(a))
    f.write(strr)


#generate_big()
#generate_time()
