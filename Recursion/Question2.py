def checkValidString(s):
    open_count = 0
    for char in s:
        if char == '(' or char == '*':
            open_count += 1
        else:
            open_count -= 1
        if open_count < 0:
            return False

    close_count = 0
    for char in reversed(s):
        if char == ')' or char == '*':
            close_count += 1
        else:
            close_count -= 1
        if close_count < 0:
            return False

    return True


s = "()"
result = checkValidString(s)
print(result)  # Output: True
