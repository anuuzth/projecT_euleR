def winner():
    pos = int(input("Enter the first participant:"))-1
    a = []
    for i in range(1,6):
        a.append(i)
    
    while(len(a)>1):
        pos += 1
        pos %= len(a)
        del(a[pos])
    print(a[0])



   
winner()
