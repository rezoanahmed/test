n1,n2 = 3,99
cont = 1
for i in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r = r + str(cont) + " "
        cont = cont + 1
    print(r[:-1])