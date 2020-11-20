sum = 0
x = int(input())
y = int(input())
temp = x
if(x>y):
    x=y
    y = temp
for i in range(x,y+1):
    if(i%13!=0):
        sum = sum + i
print(sum)