#For example, the word "listen" can be rearranged to form the word "silent," 
# which is an anagram of "listen." Similarly, the phrase "astronomer" can be 
# rearranged to form the phrase "moon starer," which is an anagram of "astronomer."


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    char_frequency = {}
    for char in str1:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for char in str2:
        if char in char_frequency:
            char_frequency[char] -= 1
            if char_frequency[char] < 0:
                return False
        else:
            return False

    return True

str1 = "listen"
str2 = "silent"
result = is_anagram(str1, str2)
print(f"Are '{str1}' and '{str2}' anagrams? {result}")