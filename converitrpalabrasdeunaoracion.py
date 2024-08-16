#Problema: Este código debería contar el número de palabras en una oración, pero no funciona como se espera.

#def contar_palabras(oracion):

#    palabras = oracion.split(",")

#    return len(palabras)

#oracion = "Este es un ejemplo de oración"

#print("Número de palabras:", contar_palabras(oracion))
            
#Explicación: El error ocurre porque el método
#split
#no está dividiendo las palabras correctamente. El separador utilizado no es el adecuado.

#Deber: Corrige el código para que cuente el número de palabras en la oración correctamente.

#Pista: Revisa qué carácter estás usando para dividir las palabras en la oración. ¿Es una coma o un espacio?


def contar_palabras(oracion):
    # Dividir la oración por espacios en blanco
    palabras = oracion.split()  # split() sin argumentos divide por cualquier tipo de espacio en blanco
    return len(palabras)

oracion = "Este es un ejemplo de oración"
print("Número de palabras:", contar_palabras(oracion))