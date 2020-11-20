total = 0
X = int(input())
Y = int(input())
if(X<Y):
	for number in range(X,Y):
		if(number%2!=0):
			total = total + number
					
elif(X>Y):
	for number in range(Y+1,X):
		if(number%2!=0):
			total = total + number	
else:
	total = 0

print(total)
