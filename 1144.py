N = int(input())
initial = 1
for i in range(N):
    print('%d %d %d'%(initial,initial**2,initial**3))
    print('%d %d %d'%(initial,initial**2+1,initial**3+1))
    initial+=1