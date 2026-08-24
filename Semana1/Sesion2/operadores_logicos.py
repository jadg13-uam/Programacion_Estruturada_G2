#Leer tres numeros y evaluar logicamente
number1 = int(input("Leer el primer valor: "))
number2 = int(input("Leer el segundo valor: "))
number3 = int(input("Leer el tercer valor: "))

#Evaluar que numero1 sea mayor a numero2 y numero1 mayor a numero 3
print(f"({number1} > {number2}) Y ({number1} > {number3}): {number1 > number2 and number1 > number3} ")


#Evaluar que numero1 sea mayor o igual que numero3 o numero3 menor que numero2
print(f"({number1} >= {number3}) O ({number2} < {number3}): {number1 >= number3 or number3 < number2} ")

#Negar que numero1 se mayor que numero 2
print(f"({number1} > {number2}): {not(number1 > number2)} ")

#asignación
number1 = 16
number1 += 14
number1 -= number2
print(f"Numero 1: {number1}")