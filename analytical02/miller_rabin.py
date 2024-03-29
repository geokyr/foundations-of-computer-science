import random

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

for i in range(100, 3000):
    if(miller_rabin(i, 30)):
        if(miller_rabin(pow(2, i) - 1, 30)):
            print("2 to the power of", i, "minus 1 is a Mersenne number.")