def print_result(func):
    def wrapper(*args, **kwargs):
        print('Название функции:', func.__name__)
        print('Результат выполнения функции:')
        res = func(*args, **kwargs)
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for i in res:
                print(i, '=', res[i])
        else:
            print(res)
        return func(*args, **kwargs)
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()


