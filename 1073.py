N = int(input())
if(5 < N < 2000):
        for a in range(1,N+1):
                if(a%2==0):
                        print('%d^2 = %d' %(a,a**2))
