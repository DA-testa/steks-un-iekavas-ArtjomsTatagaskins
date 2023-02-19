# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"
            


def main():
    letter = input("F or I?")
    if "F" in letter:
        filename = input("File name?")
        with open(filename, "r") as file:
            brackets = file.read()
        print(find_mismatch(brackets))
    elif "I" in letter:
        brackets = input()
        print(find_mismatch(brackets))
    else: print("input error")

if __name__ == "__main__":
    main()
