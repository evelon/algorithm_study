import random
import string

def createKeyString(TEST_VALUE_LEN):
    list = []
    letters = string.ascii_letters + string.digits
    key = ''.join(random.choice(letters) for i in range(5 + random.randint(5, 5)))
    list.append(key)
    for i in range(0, TEST_VALUE_LEN):
        value = random.randint(-2147483648, 2147483647)
        list.append(str(value))
    return ' '.join(list)


def __MAIN__():
    f = open('test_input', 'w')
    TEST_MAX = 100000
    TEST_LINE_VALUE_MAX = 10
    for i in range(0, TEST_MAX):
        f.write(createKeyString(TEST_LINE_VALUE_MAX))
        f.write('\n')
    f.close()
    return 0

__MAIN__()