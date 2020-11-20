age = int(input())

year = int(age/365)
month = int((age%365)/30)
days = (age%365)%30

print(year,'ano(s)')
print(month,'mes(es)')
print(days,'dia(s)')