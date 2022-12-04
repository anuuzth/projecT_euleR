def primefactors(n):
    divisor = 2
    array = []
    while divisor <= n:
        if n % divisor == 0:
            array.append(divisor)
            n = n/divisor
        else:
            divisor += 1
            
    return(array)

def largest_primefactor():
    n = int(input("enter the number to find largest prime_factor of:"))
    a = primefactors(n)
    largest = a[0]
    for element in a:
        if element > largest:
            largest = element
    print(largest)


largest_primefactor()