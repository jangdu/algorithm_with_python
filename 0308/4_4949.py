
pair = {
        '{': '}',
        '(' : ')',
        '[': ']',
    }
opener = "({["
closer = "}])"
stack = []
 
while True:
    sentence = input()
    if sentence == '.':
        break

    for i in sentence:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                print("no")
                break
            else:
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                print("no")

                break
            else:
                stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')

    stack.clear()