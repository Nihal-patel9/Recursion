def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:

        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    differences = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            differences.append(i)

    return len(differences) == 2 and s[differences[0]] == goal[differences[1]] and s[differences[1]] == goal[differences[0]]


s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  # Output: True
