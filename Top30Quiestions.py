test_input = "hi"

test_input1 = "wow"

def isPalindrome(str):
    tmp = ""
    for i in range(0, len(str)):
        tmp += str[len(str) - 1 - i]
        print tmp
    return tmp == str

print isPalindrome(test_input)
print isPalindrome(test_input1)


def removeLetter(remove, str):
    tmp = ""
    for i in range(0, len(str)):
        if str[i] != remove:
            tmp += str[i]
    return tmp

print removeLetter("e", test_input)
print removeLetter("w", test_input1)