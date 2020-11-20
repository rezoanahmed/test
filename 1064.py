positives = 0
total = 0
for i in range(6):
	number = float(input())
	if(number>0):
		positives = positives + 1
		total = total + number
avarage = total / positives
print(positives,'valores positivos')
print('%.1f'%avarage)
