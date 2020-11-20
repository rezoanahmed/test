N = float(input())
dollars = int(N)
cents = N - dollars

#Dollars
hundred = int(dollars/100)
fifty = int((dollars%100)/50)
twenty = int(((dollars%100)%50)/20)
ten = int((((dollars%100)%50)%20)/10)
five = int(((((dollars%100)%50)%20)%10)/5)
two = int((((((dollars%100)%50)%20)%10)%5)/2)
one = int((((((dollars%100)%50)%20)%10)%5)%2)

#Cents
fiftycents = int(cents/.50)
twentyfivecents = int((cents%.50)/.25)
tencents = int(((cents%.50)%.25)/.10)
fivecents = int((((cents%.50)%.25)%.10)/.05)
onecents = int(((((cents%.50)%.25)%.10)%.05)/0.01)

print("NOTAS:")
print(hundred,'nota(s) de R$ 100.00')
print(fifty, 'nota(s) de R$ 50.00')
print(twenty, 'nota(s) de R$ 20.00')
print(ten, 'nota(s) de R$ 10.00')
print(five, 'nota(s) de R$ 5.00')
print(two, 'nota(s) de R$ 2.00')
print("MOEDAS:")
print(one, 'moeda(s) de R$ 1.00')
print(fiftycents, 'moeda(s) de R$ 0.50')
print(twentyfivecents, 'moeda(s) de R$ 0.25')
print(tencents, 'moeda(s) de R$ 0.10')
print(fivecents, 'moeda(s) de R$ 0.05')
print(onecents, 'moeda(s) de R$ 0.01')