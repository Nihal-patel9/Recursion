def decodeString(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ""
            curr_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += char

    return curr_str


s = "3[a]2[bc]"
decoded_string = decodeString(s)
print(decoded_string)  # Output: "aaabcbc"
