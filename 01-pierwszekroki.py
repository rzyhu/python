#stan_konta = input("Podaj stan konta")
#stan_konta = int(stan_konta)
#stan_konta = stan_konta + 500*2
#print(stan_konta)

x = 9
y = x/2
x = x**(1/2)
print(x)

temperature = 15
czy_szczesliwy = True
if temperature > 10 or czy_szczesliwy:
    print("wychodzimy")
elif temperature > -10 and czy_szczesliwy:
    print("ubierz sie cieplo")
else:
    print("nie wychodzimy")


for i in range(1,10,2):
    if i == 5:
        break
    print(i)

while temperature > 10:
    print("temperatura jest okej", temperature)
    temperature -= 1