n = int(input())
l = input()   # takes the whole line of n numbers
a = list(map(int,l.split())) # split those numbers with space and map as integer
minimum = min(a)
# print(minimum)
position = a.index(minimum)
# print(position)
print("Menor valor: %d" %minimum)
print("Posicao: %d" %position)