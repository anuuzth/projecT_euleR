def is_divisible(num):
    for i in range(2,21):
        if num % i !=0:
            return False
    return True

def divisiblebyall():
    num = 2520
    while True:
        if is_divisible(num):
            break
        num +=1
    print(num)

divisiblebyall()