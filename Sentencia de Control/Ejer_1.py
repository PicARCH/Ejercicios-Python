'''
1. Ejercicio: Verificación de edad para ingresar a una fiesta:
   - Escribir un programa que solicite al usuario su edad.
   - Si la edad es mayor o igual a 18, imprimir "¡Bienvenido/a a la fiesta!"
   - Si la edad es menor a 18, imprimir "Lo siento, debes ser mayor de edad para ingresar."

   Casos de prueba:
   - Entrada: 20
     Salida: ¡Bienvenido/a a la fiesta!
   - Entrada: 16
     Salida: Lo siento, debes ser mayor de edad para ingresar.
'''
edad=int(input("Ing. edad: "))
if edad >=18:
    print("¡Bienvenido/a a la fiesta!")
else:
    print("Lo siento, debes ser mayor de edad para ingresar.")