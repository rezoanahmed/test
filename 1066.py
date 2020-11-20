even = 0
odd = 0
positive = 0
negative = 0
for i in range(5):
	number = int(input())
	if(number%2==0):
		even = even + 1
	if(number%2!=0):
		odd = odd + 1
	if(number>0):
		positive = positive + 1
	if(number<0):
		negative = negative + 1
print(even,'valor(es) par(es)')
print(odd,'valor(es) impar(es)')
print(positive,'valor(es) positivo(s)')
print(negative,'valor(es) negativo(s)')
