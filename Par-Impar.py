print("Bienvenido a Par o Impar.")

try:
    num = int(input("Por favor, ingrese un número: "))
except(ValueError, NameError):
    print("Haz ingresado un valor NO valido.")
    num = int(input("Por favor, ingrese un número entero: "))

while num != 00:
    if num%2 == 0:
        print("El número es PAR.")
    else:
        print("El número es IMPAR.")
#Aca coloco otro try, except por si en una de las repeticiones el usuario se vuelve a equivocar
    try:
        num = int(input("Ingrese otro número o \"00\" para salir: "))
    except(ValueError, NameError):
        print("Haz ingresado un valor NO valido.")
        num = int(input("Por favor, ingrese un número entero: "))

print("Haz salido del programa, gracias por participar.")