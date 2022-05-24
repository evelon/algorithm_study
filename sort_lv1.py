import sys
from unittest import TextTestResult

def read_test_input(TEST_MAX):
    result = []
    f = open("test_input", 'r')
    with f as obj:
        for [_, line] in zip(range(TEST_MAX) , obj):
            list = []
            line = line.strip()
            key, *value_as_string = line.split(' ')
            list.append(key)
            list.extend(map(int, value_as_string))
            result.append(list)
    f.close()
    return result

def keyCompare(elem1, elem2):
    if elem1[0] == elem2[0]:
        return 0
    if elem1[0] < elem2[0]:
        return 1
    if elem1[0] > elem2[0]:
        return -1

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]

def sort_lv1(input_list):
    if (keyCompare(input_list[0], input_list[1]) == -1):
        swap(input_list, 0, 1)
    if (keyCompare(input_list[1], input_list[2]) == -1):
        swap(input_list, 1, 2)
    if (keyCompare(input_list[0], input_list[1]) == -1):
        swap(input_list, 0, 1)

def __MAIN__():
    TEST_MAX = int(sys.argv[1])
    input_list = read_test_input(TEST_MAX)
    print(input_list)
    sort_lv1(input_list)
    print(input_list)
    return 0

__MAIN__()