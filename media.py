n1 = float(input('Digite um numero '))
n2 = float(input('Digite outro numero '))
n3 = float(input('Digite outro numero '))

media = (n1+n2+n3)/3
print(media)
if(media >= 9):
    print('Sua nota foi boa')
elif(media >= 6):
    print('Sua nota foi regular')
else:
    print('Sua nota foi ruim')