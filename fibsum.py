
def fib():
    array = [1]
    a =1
    b =2
    while b < 4000000:
            array.append(b)
            c = a + b
            a = b
            b = c
    return(array)   
   
def sum():
    arr = fib()
    
    sum = 0
    for element in range(len(arr)):
        if arr[element]%2 == 0 :
            sum = sum + arr[element]
    print(sum)


sum()