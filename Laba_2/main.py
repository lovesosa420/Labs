from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


def main():
    r = Rectangle("синего", 15, 15)
    c = Circle("зеленого", 15)
    s = Square("красного", 15)
    print(r)
    print(c)
    print(s)


if __name__ == "__main__":
    main()