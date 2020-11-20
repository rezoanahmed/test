N = int(input())
In = 0
Out = 0
for n in range(N):
	X = int(input())
	if(X>=10 and X<=20):
		In = In + 1
	else:
		Out = Out + 1
print(In,'in')
print(Out,'out')
