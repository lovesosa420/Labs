def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for arg in args:
            for i in range(len(items)):
                for j in items[i]:
                    if j == arg and items[i][j] != None:
                        yield items[i][j]
    else:
        for i in range(len(items)):
            d = {}
            for arg in args:
                for j in items[i]:
                    if j == arg and items[i][j] != None:
                        d[j] = items[i][j]
            yield d


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    x = field(goods, 'title', 'color')
    for i in range(len(goods)):
        if i != len(goods) - 1:
            print(next(x), end=', ')
        else:
            print(next(x))
