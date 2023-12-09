op = input("Caso queira fazer um calculo digite SIM ")

while op == "SIM":
    print("Selecione a opção desejada")

operacao = input("Qual operação você deseja realizar? ")

if(operacao == "+"):
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    adicao = n1 + n2
    print(adicao)
    
if(operacao == "-"):
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    subtracao = n1 - n2
    print(subtracao)
     
if(operacao == "x"):
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    multiplicacao = n1 * n2
    print(multiplicacao)

if(operacao == "/"):
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    divisao = n1 / n2
    print(divisao)

