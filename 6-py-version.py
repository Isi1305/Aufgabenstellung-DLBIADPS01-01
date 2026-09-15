# Google Hilfe
number = 12
factors = [i for i in range(1, number + 1) if number % i == 0]
print(factors)

# Meine Version
for i in range(1, 13):
    if 12 % i == 0:
        print(i)

# Für das Verständnis zwischen imperativ und deklarativ: C (imperativ) und Haskell (funktional)