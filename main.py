import test
from test import print_list_items
from test import a as ta
# from test import *

from utils.get_file_data import read_file
from Package1 import *



def main():
    """
    Circular Import
    """
    a = 27
    print(a)
    # print(ta)
    print_list_items([1, 2, 3, 4, 5])
    # print('hello')

    print(read_file('a.txt'))
    print(func1())
    try:
        number = int(input('Enter Number: '))
        a = [1, 2]

        # a[5]
        '25' + 2
        print(number)
    except ValueError:
        print('User Tried to enter non integer value!')
    except Exception:
        print('User Tried to access non existent index!')

    print('lalalalal')


if __name__ == '__main__':
    print(__name__)
    main()
