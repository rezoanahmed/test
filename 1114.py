password = 2002
while True:
    correctPass = int(input())
    if(password==correctPass):
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')