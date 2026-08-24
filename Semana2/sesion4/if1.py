#Leer la nota de un estudiante y decir si aprobo o reprobo
from colorama import Fore, Style

grade = int(input("Ingresa la nota: "))

if(grade >= 70):
    print(Fore.GREEN + "Usted esta aprobado.")
else:
    print(Fore.RED + "Su aprendizaje es inicial.")
print(Style.RESET_ALL)