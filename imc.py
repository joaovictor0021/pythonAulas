altura = input("Digite sua altura ")
peso = input("Digite seu peso ")

bmi = (altura / (peso * peso))**2

if(bmi < 18.5): 
    print("Cuidado! Você está abaixo do peso!")
elif(bmi >= 18.5 & bmi <= 25):
    print("Você está no peso ideal!")
elif(bmi > 25 & bmi <= 35):
    print("Cuidado! Você está com sobrepeso!")
elif(bmi > 35 & bmi <= 40):
    print("Você está com obesidade severa!")
else:
    print("Cuidado! Você está com obesidade morbida!")
