s = "man, a plan, a canal: Panama"


def check_valid_palindrome(s):
    s = s.lower()
    st = "".join(char for char in s if char.isalnum())
    left = 0
    right = len(st) - 1

    while left < right:
        if st[left] != st[right]:
            return False
        left += 1
        right -= 1
    return True


print(check_valid_palindrome(s))
