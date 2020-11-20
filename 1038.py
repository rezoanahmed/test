X, Y = input().split()
if (int(X) == 1):
	bill = 4.00 * int(Y)
elif(int(X) == 2):
	bill = 4.50 * int(Y)
elif(int(X) == 3):
	bill = 5.00 * int(Y)
elif(int(X) == 4):
	bill = 2.00 * int(Y)
elif(int(X) == 5):
	bill = 1.50 * int(Y)
print('Total: R$','%.2f'%bill)