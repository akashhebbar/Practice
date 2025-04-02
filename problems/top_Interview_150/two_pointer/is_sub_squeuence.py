s = "ac"
t = "ahbgdc"


def check_sub_sequence(s, t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True

    s_pointer = 0  # pointer for string s

    # Check each character in t
    for t_char in t:
        # If we find a match, move s_pointer
        if s_pointer < len(s) and s[s_pointer] == t_char:
            s_pointer += 1
        # If we've matched all characters in s
        if s_pointer == len(s):
            return True

    return s_pointer == len(s)


print(check_sub_sequence(s, t))

print(check_sub_sequence("abc", "ahbgdc"))  # True
print(check_sub_sequence("axc", "ahbgdc"))  # False
print(check_sub_sequence("", "ahbgdc"))  # True
print(
    check_sub_sequence("abc", "bac")
)  # False (original would return True incorrectly)
