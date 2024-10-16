print(" ")#define una linea en blanco
print("3- Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta, un número de kilos mostrar el precio de ese número de kilos de fruta.")
print(" ")#define una linea en blanco
print("Roman De la Cruz leonardo Antonio.3-w.1211")
print(" ")#define una linea en blanco
#define variable y valores
valor = {
    'uvas': 23,
    'kiwi': 33,
    'platano': 24,
    'mango': 89,
}

#solicita lo deseado
ft = input("Ingrese la fruta: ")
kl = float(input("Ingrese el número de kilos: "))

#imprime el precio o si hay un error
if ft in valor:
    total = valor[ft] * kl
    print("El precio de", kl, "kilos de", ft, "es", total, "pesos")
else:
    print("La fruta", ft, "no está en el diccionario.")
print(" ")#define una linea en blanco