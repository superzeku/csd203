def pow(x,n):
    if n < 0: return 1/pow(x,-n)
    if n == 0: return 1
    if n%2 == 1: return x*pow(x,n-1)
    return x*pow(x,n//2)
#print(pow(2,-3))

def checkpalindrome(n):
    if len(n) == 1: return True
    if len(n) == 2:
        return n[0] == n[1]
    if n[0] != n[-1]:
        return False
    return checkpalindrome(n[1:-1])

n = 123321
print(checkpalindrome(str(n)))