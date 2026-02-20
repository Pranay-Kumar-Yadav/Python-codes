#balanced brackets
def is_balanced(expression):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        if char in pairs.values():  # opening brackets
            stack.append(char)
        elif char in pairs.keys():  # closing brackets
            if stack == [] or stack.pop() != pairs[char]:
                return False

    return stack == []


#input from user
expr = input("Enter expression: ")

if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")