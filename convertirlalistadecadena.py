#Problema: El siguiente código debería combinar todas las cadenas de una lista en una sola cadena, separadas por un espacio, pero está agregando un espacio extra al final.

#def combinar_cadenas(lista):

#    cadena = ""

#    for palabra in lista:

#        cadena += palabra + " "

#    return cadena

#lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

#print("Cadena combinada:", combinar_cadenas(lista_cadenas))
            
#Explicación: El problema es que se agrega un espacio extra al final de la cadena combinada. Necesitas corregir esto para que la cadena final no tenga un espacio adicional al final.

#Deber: Corrige el código para que la cadena combinada no tenga un espacio extra al final.

#Pista: Piensa en cómo puedes manejar el espacio entre las palabras para que no se agregue uno extra al final.


def combinar_cadenas(lista):
    # Unir todas las cadenas de la lista con un espacio como separador
    return " ".join(lista)

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))