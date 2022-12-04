def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return(rev)

def pallindrome():
    a = []
    for i in range(100,1000):
        for j in range(100,1000):
            x = i*j 
            if x == reverse(x):
                a.append(x)
    return(a)

def largest_pallindrome():
    a = pallindrome()
    largest = a[0]
    for element in a:
        if element > largest:
            largest = element
    print(largest)
        

largest_pallindrome()

