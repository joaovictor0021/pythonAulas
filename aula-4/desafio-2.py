valor = float(input("Digite um valor menor que 10 ou maior que 100: "))

if 10 <= valor <= 100:
    for i in range(valor + 1):
        print(i)
else:
    print("Insira um valor válido")