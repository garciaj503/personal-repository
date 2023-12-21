def isPalindrome(x):
    y = str(x)
    z = y[::-1]
    print(type(z))
    print(type(x))
    if str(x) == z:
        return True
    else:
        return False
    
print(isPalindrome(121))
isPalindrome(121)