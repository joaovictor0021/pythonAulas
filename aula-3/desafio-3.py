print("insira dois números para ver se o primeiro número é multiplo do segundo")

n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))

if (n1 % n2 == 0):
    print("O número", n1, "é multiplo do número", n2)
else:
    print("O número", n1, "não é multiplo do número", n2)