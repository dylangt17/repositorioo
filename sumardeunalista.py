#Problema: Este código debería invertir una cadena (es decir, escribirla al revés), pero produce un resultado incorrecto.


#def invertir_cadena(cadena):

#    invertida = ""

#    for i in range(len(cadena)):

#       invertida += cadena[i-1]

#    return invertida



#cadena = "Python"

#print("Cadena invertida:", invertir_cadena(cadena))
            
#Explicación: El problema radica en la forma en que se está manejando el índice para acceder a los caracteres de la cadena.

#Deber: Corrige el código para que invierta correctamente cualquier cadena.

#Pista: Piensa en cómo puedes acceder a los caracteres de la cadena desde el último hasta el primero.


def invertir_cadena(cadena):
    invertida = ""
    longitud = len(cadena)
    
    for i in range(longitud):
        invertida += cadena[longitud - 1 - i]  # Acceder al carácter desde el final hacia el principio

    return invertida

cadena = "Python"
print("Cadena invertida:", invertir_cadena(cadena))