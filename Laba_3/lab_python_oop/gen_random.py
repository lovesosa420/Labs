from random import randint


def gen_random(num_count, begin, end):
    l = []
    for i in range(num_count):
        y = ', зарплата ' + str(randint(begin, end)) + ' руб'
        l.append(y)
    return l

# gen_random(100000, 200000)
