def compress(chars):
    write_idx = 0
    curr_idx = 0

    while curr_idx < len(chars):
        char = chars[curr_idx]
        count = 1

        while curr_idx + 1 < len(chars) and chars[curr_idx + 1] == char:
            count += 1
            curr_idx += 1

        chars[write_idx] = char
        write_idx += 1

        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write_idx] = digit
                write_idx += 1

        curr_idx += 1

    return write_idx


chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)  # Output: 6
print(chars[:new_length])  # Output: ["a", "2", "b", "2", "c", "3"]
