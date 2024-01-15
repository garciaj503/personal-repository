def isPalindrome(x):
    y = str(x)
    z = y[::-1]
    if str(x) == z:
        return True
    else:
        return False
    
print(isPalindrome(121))