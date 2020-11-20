#Prime Numbers
#eh primo if prime number
#nao eh primo if not prime
N = int(input())
for i in range(N):
    X = int(input())
    prime = True

    for i in range(2,X):
        if(X%i==0):
            prime = False
            break
    if(prime):
        print('%d eh primo' %(X))
    else:
        print('%d nao eh primo' %(X))
