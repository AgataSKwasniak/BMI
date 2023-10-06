a = float(input("Podaj wzrost w metrach: "))
b = int(input("Podaj wage: "))
c=b/(a**2)

if c>=18.5 and c<=24.9:
    print("waga prawidlowa")
elif c<18.5:
    print("niedowaga")
elif c>24.9:
    print("nadwaga")



