data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


def sort(data):
    result = sorted(data)[::-1]
    print(result)

    result_with_lambda = sorted(data, key=lambda x: -x)
    print(result_with_lambda)


sort(data)

