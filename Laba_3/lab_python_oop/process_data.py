import json
import sys
from lab_python_fp.print_result.print_result import print_result
from lab_python_fp.cm_timer.cm_timer import cm_timer_1
from lab_python_fp.unique.unique import Unique
from lab_python_fp.gen_random.gen_random import gen_random
path = "data_light.json"


with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)


def Filter(x):
    if x['job-name'][0:11].lower() == 'программист':
        return True
    else:
        return False


@print_result
def f1(arg):
    return sorted([x for x in Unique([x.get('job-name') for x in arg], ignore_case=True)])


@print_result
def f2(arg):
    return list(filter(lambda x: x[0:11].lower() == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    zipped = list(zip(arg, gen_random(len(arg), 100000, 200000)))
    return [x + str(y) for x, y in zipped]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

