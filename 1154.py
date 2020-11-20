total = 0
people = 0
while True:
    age = int(input())
    if (age<0):
        break
    total = total + age
    people+=1
    age+=1
    avarage = total / people

print('%.2f'%avarage)