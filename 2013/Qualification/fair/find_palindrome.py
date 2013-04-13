__author__ = 'Bill'

def is_palindrome_slow(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = int(num / 10)

    if n == rev:
        return True
    else:
        return False

def is_palindrome_short(s):
    s = str(s)
    length = len(s)
    for i in range(0,int(length/2)):
        if s[i] != s[(length-1)-i]: return False
    return True

def is_palindrome_reverse(s):
    s = str(s)
    return s == s[::-1]

def find_all_palindromes(left=1, right=10 ** 100):
    result = []
    for i in range(left, right):
        if is_palindrome_reverse(i):
            result.append(i)

    return result

if __name__ == '__main__':
    all_pals = find_all_palindromes(1, 10**10)
    print(len(all_pals), all_pals)