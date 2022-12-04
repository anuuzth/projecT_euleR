def is_prime(n):
    for i in range(2,1+int(n/2)):
        if n%i==0:
            return False
    return True

    
def nthprime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n-=1
        i += 1
    i -= 1

    return i

print(nthprime(10001))