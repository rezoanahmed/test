start,end = input().split()
if(int(start)==int(end)):
	time = 24
elif(int(start)>int(end)):
	time = 24 - (int(start) - int(end))
elif(int(start)<int(end)):
	time = int(end) - int(start)
print('O JOGO DUROU', time, 'HORA(S)')
