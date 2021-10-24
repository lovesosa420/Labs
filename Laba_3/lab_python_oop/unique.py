

class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self.set = set()
        self.items = items
        self.ic = ignore_case
        self.it = iter(self.items)

    def __next__(self):
        while True:
            try:
                current = next(self.it)
                if self.ic == True and isinstance(current, str):
                    temp = current[:]
                    if temp.lower() not in self.set:
                        self.set.add(temp.lower())
                        return current
                else:
                    if current not in self.set:
                        self.set.add(current)
                        return current
            except StopIteration:
                raise

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = ['A', 'a', 'b', 'B', 'a', 'A', 'b', 1, 2, 1]
    x = Unique(data, ignore_case=True)
    for i in Unique(x):
        print(i)
#
