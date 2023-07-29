'''
2. Ejercicio: Cálculo del descuento de un producto:
   - Escribir un programa que solicite al usuario el precio de un producto y su categoría (A, B o C).
   - Si la categoría es A, aplicar un descuento del 20% al precio.
   - Si la categoría es B, aplicar un descuento del 10% al precio.
   - Si la categoría es C, no aplicar ningún descuento.
   - Imprimir el precio final con el descuento aplicado.

   Casos de prueba:
   - Entrada: Precio = 100, Categoría = A
     Salida: Precio final: 80
   - Entrada: Precio = 50, Categoría = B
     Salida: Precio final: 45
   - Entrada: Precio = 75, Categoría = C
     Salida: Precio final: 75
FORMULA
La fórmula para calcular el descuento de un producto es:

Descuento = Precio * (Porcentaje de descuento / 100)

Donde:
- Descuento es el valor del descuento a aplicar al precio del producto.
- Precio es el precio original del producto.
- Porcentaje de descuento es el porcentaje de descuento que se aplicará al precio.
'''
precio=float(input("ing. precio: "))
categoria=input("ing. Categoria A,B o C: ")
if categoria=="A" or categoria=="B" or categoria=="C" :
    if categoria == "A":
        descuento= precio*(20/100)
        precioFinal=precio - descuento
    elif  categoria == "B":
        descuento = precio*(10/100)
        precioFinal = precio - descuento
    elif categoria == "C":
        descuento =precio
    if descuento.is_integer():
        print("Precio Final: ",int(descuento))#2
    else:
        print("Precio Final: ", descuento)#2.3


else:
    print("ingresate categoria incorecta!")
