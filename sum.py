#sum of no.s divisible by 3 or 5 in range 1 to below 1000
def sum():
    sum = 0
    for i in range(1, 1000):
       if i % 5 == 0 or i % 3 == 0:
        sum += i
    print(sum)
    
sum()

