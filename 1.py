print(" ")#define una linea en blanco
print(" 1- Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, El usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.")
print(" ")#define una linea en blanco
print("Roman De la Cruz leonardo Antonio.3-w.1211")
print(" ")#define una linea en blanco
diccionario_divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}#definicion de cada variable

divisa = input("Ingrese una divisa: ")#solicita al usuario la vaiable

print(" ")#define una linea en blanco
if divisa in diccionario_divisas:
    print("El símbolo de", divisa, "es", diccionario_divisas[divisa])#imrpime lo escrito
else:
    print(" ")#define una linea en blanco
    print("La divisa", divisa, "no está en el diccionario.")#imprime si hay errorprint
    print(" ")#define una linea en blanco