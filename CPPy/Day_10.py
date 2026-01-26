# fibonacci series normal
def gen_fibo(index):
    fibo = []
    for a in range(0,index):
        if a == 0:
            fibo.append(a)
        elif a == 1:
            fibo.append(a)
        else:
            fibo.append(fibo[a - 2] + fibo[a - 1])
    print(fibo)

gen_fibo(4)

# fibonacci series with less omplexity
def gen_fibo_advanced(index):
    a, b = 0, 1
    fibo = []
    for _ in range(0,index):
        fibo.append(a)
        a, b = b, a + b
    return fibo
    
print(gen_fibo_advanced(4))
