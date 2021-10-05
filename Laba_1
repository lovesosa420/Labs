import math
import sys


def solution(a, b, c, k):
    x = float()
    D = b**2 - 4*a*c
    if D > 0:
        for i in range(2):
            x = (- b + ((-1) ** i) * math.sqrt(D)) / (2 * a)
            if x > 0:
                k.append(math.sqrt(x))
                k.append(-math.sqrt(x))
            elif x == 0:
                k.append(math.sqrt(x))
    elif D == 0:
        x = - b / (2 * a)
        if x > 0:
            k.append(math.sqrt(x))
            k.append(-math.sqrt(x))
        elif x == 0:
            k.append(math.sqrt(x))


def get_coef(index, promt, m):
    try:
        coef = sys.argv[index]
        coef = float(coef)
    except:
        while True:
            try:
                coef = float(input())
                if len(m) == 0:
                    if coef == 0:
                        print(promt)
                        continue
                    m.append('епт')
                break
            except ValueError:
                print(promt)
    return coef


def main():
    k, m = [], []
    a = get_coef(1, 'Введите ненулевой коэффициент a!', m)
    b = get_coef(2, 'Введите коэффициент b!', m)
    c = get_coef(3, 'Введите коэффициент c!', m)
    solution(a, b, c, k)
    if len(k) == 0:
        print('Нет корней!')
    else:
        for i in range(len(k)):
            print(i+1, 'корень уравнения:', k[i])


if __name__ == "__main__":
    main()
