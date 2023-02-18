# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(i+1)
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            stack_length = opening_brackets_stack.__len__()
            if stack_length == 0:
                return i+1

            idx = stack_length-1
            last_bracket = opening_brackets_stack[idx]
            if are_matching(last_bracket, next):
                opening_brackets_stack.pop()
                opening_brackets_stack.pop()
            else:
                return i+1
            pass
        

    if opening_brackets_stack.__len__() > 0:
        opening_brackets_stack.pop()
        return opening_brackets_stack.pop()

    return -1


def main():
    text = input()
    if "I" in text:
        text2= input()
        mismatch = find_mismatch(text2)
    if "F" in text:
        pass
    if mismatch < 0 and text.__len__() <= 105:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
