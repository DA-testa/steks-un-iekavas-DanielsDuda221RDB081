# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # print(next)
        # print(opening_brackets_stack)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(i+1)
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            stack_length = opening_brackets_stack.__len__()
            if stack_length == 0:
                # mismatch
                # print("exit 1")
                return i+1

            idx = stack_length-1
            last_bracket = opening_brackets_stack[idx]
            # print("last:"+last_bracket)
            if are_matching(last_bracket, next):
                # match
                opening_brackets_stack.pop()
                opening_brackets_stack.pop()
            else:
                # mismatch
                # print("exit 2")
                return i+1
            # change2
            pass

    if opening_brackets_stack.__len__() > 0:
        opening_brackets_stack.pop()
        return opening_brackets_stack.pop()

    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch < 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
