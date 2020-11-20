#-------------------------------While Loop--------------------------
N = int(input())
i = N
while i>=1:
    # N = N * i
    i = i - 1
    if(i>=1):
        N = N * i
print(N)

#------------------------------For Loop-------------------------------
n = int(input())
r = 1
for i in range(1,n+1):
    r = r*i
print(r)