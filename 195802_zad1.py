#!/usr/bin/env python
WELCOME = "Mastermind by Damian Nogaj\n" \
          "# - exist, but wrong position\n" \
          "@ - exist and correct position\n" \
          "Allow characters: a, b, c, d, e, f, g, h/n"
import random
ALLOWCHARS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


def check_str(answ):
    """
    Checking input string
    :param answer: input answer
    """
    correct_chars = 0
    if len(answ) == 4:
        for itr in range(4):
            if 97 <= ord(answ[itr]) <= 104:
                correct_chars += 1
        if correct_chars == 4:
            return True
        else:
            return False
    else:
        return False


def gen_code():
    """
    Generating code
    return generated code
    """
    code = ''
    for aitr in range(4):
        code += random.choice(ALLOWCHARS)
        aitr = aitr
    return code


def compare(code, answer):
    """
    Comparing code and answer
    :param code:
    :param answer:
    return list [good position, exist in]
    """
    monkey = 0
    hashe = 0
    for uit in range(4):
        if code[uit] == answer[uit]:
            monkey += 1
        elif answer[uit] in code:
            hashe += 1
    return [monkey, hashe]
if __name__ == '__main__':
    print(WELCOME)
    CODE = gen_code()
    level = 0
    while level <= 8:
        level += 1
        print('Try %s. Write answer:' % level)
        INP = input()
        if check_str(INP):
            RESULT = compare(CODE, INP)
            A = 0
            B = 0
            while RESULT[0] > A:
                print('@')
                A += 1
                B += 1
            while RESULT[1] > B:
                print('#')
                B += 1
            if level == 8:
                print('You lose!!!')
                print('Correct code is:%s' % CODE)
                break
            if RESULT[0] == 4:
                print('You WIN!')
        else:
            print('Niedozwolone znaki')
            if level > 1:
                level -= 1
            else:
                level = 0
