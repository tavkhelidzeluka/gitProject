import test
from test import print_list_items
from test import a as ta

from utils.get_file_data import read_file


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


if __name__ == '__main__':
    print(__name__)
    main()
