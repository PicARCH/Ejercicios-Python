'''
Ejercicio: Evaluación de aprobación en un curso:
   - Escribir un programa que solicite al usuario su calificación en un curso (0-100).
   - Si la calificación es mayor o igual a 70, imprimir "¡Felicidades! Has aprobado el curso."
   - Si la calificación es menor a 70, imprimir "Lo siento, has reprobado el curso."
   - Si la calificación es mayor a 100 o menor a 0, imprimir "Calificación inválida."

   Casos de prueba:
   - Entrada: 85
     Salida: ¡Felicidades! Has aprobado el curso.
   - Entrada: 60
     Salida: Lo siento, has reprobado el curso.
   - Entrada: 110
     Salida: Calificación inválida.
'''
calificacion=int(input("Ing. tu calificacion (0-100):"))
if calificacion >= 0 and calificacion <= 100:
    if calificacion >= 70:
        print("¡Felicidades! Has aprobado el curso.")
    else:
        print("Lo siento, has reprobado el curso.")
else:
    print("Calificación inválida.")

