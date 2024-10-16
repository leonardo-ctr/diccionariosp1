print(" ")#define una linea en blanco
print("2- Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>")
print(" ")#define una linea en blanco
print("Roman De la Cruz leonardo Antonio.3-w.1211")
print(" ")#define una linea en blanco
#solicita los datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")
print(" ")#define una linea en blanco
#almacena la informaicon
datos = {'nombre': nombre, 'edad': edad, 'dirección': direccion, 'teléfono': telefono}
print(" ")#define una linea en blanco
#imprime la informacion
print(datos['nombre'], "tiene", datos['edad'], "años, vive en", datos['dirección'], "y su número de teléfono es", datos)
print(" ")#define una linea en blanco