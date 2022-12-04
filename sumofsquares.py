def sumofsquares():
    sum = 0
    for i in range(1,101):
        sum = sum + i*i
    return(sum)

def squareofsum():
    sum = 0
    for i in range(1,101):
        sum += i   
    x = sum*sum
    return(x)

def final():
    x =sumofsquares()
    y = squareofsum()
    z = y - x
    print(z)

final()
