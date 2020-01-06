# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


"""
Here's what Im thinking...
Have a stack
    - if ([{, add that character to stack
    - if )]}, pop from stack. If symbol mathes its opposite, continue
                              If it doesn't, return false.
"""

from queue import LifoQueue

if __name__ == "__main__":

    string = "([])[]({})"

    stack = LifoQueue(maxsize=250)

    if len(string) == 1:
        print(f"'{string}' is unbalanced....")
        exit()

    for x in string:
        if x in ["(", "{", "["]:
            stack.put(x)
        elif x in [")", "}", "]"]:
            if stack.qsize() != 0:
                check = stack.get_nowait()
            else:
                print(f"'{string}' is unbalanced....")
                exit()

            if x == ")" and check != "(":
                print(f"'{string}' is unbalanced....")
                exit()
            if x == "]" and check != "[":
                print(f"'{string}' is unbalanced....")
                exit()
            if x == "}" and check != "{":
                print(f"'{string}' is unbalanced....")
                exit()

    print(f"'{string}' is Balanced!")

