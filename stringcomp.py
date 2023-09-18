def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        # Check if the current character is the same as the next character
        if i < len(string) - 1 and string[i] == string[i + 1]:
            count += 1
        else:
            compressed_string += string[i] + str(count)
            count = 1
    return compressed_string

input_string = "aaabbbbccccc"
compressed = compress_string(input_string)
print(compressed)  # Output: "a3b4c5"
