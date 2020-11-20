greatest = input().split(' ')
a,b,c = greatest
MaoirAB = (int(a)+int(b)+ abs(int(a)-int(b)))/2
MaoirABC = (int(MaoirAB)+int(c)+ abs(int(MaoirAB)-int(c)))/2

print(int(MaoirABC), 'eh o maior')
