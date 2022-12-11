def sum():
    for i in range(300):
        for j in range(400):
            for k in range(500):
                if   k*k == i*i + j*j:
                    if (k+i+j == 1000):
                        print(f"{k*i*j}")
                    

sum()
