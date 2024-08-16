
#def calcular_promedio(numeros):

#   suma = 0
# for numero in numeros:

 #    suma += numero

 #promedio = suma / len(numeros)

 #return promedio

#lista_numeros = [10, 20, 30, 40, 50]

#print("El promedio es:", calcular_promedio(lista_numeros))
            
#Explicación: Este error ocurre cuando la lista de números está vacía. Tu tarea es corregir el código para manejar este caso y evitar la división por cero.

#Deber: Modifica el código para que, si la lista está vacía, devuelva un mensaje que diga "La lista está vacía" en lugar de intentar calcular el promedio.

#Pista: Usa una condicional
#if
#para verificar si la lista tiene elementos antes de intentar calcular el promedio.


def calcular_promedio(numeros):
    # Verificar si la lista está vacía
    if len(numeros) == 0:
        return "La lista está vacía"
    
    suma = 0
    for numero in numeros:
        suma += numero

    promedio = suma / len(numeros)
    return promedio

lista_numeros = [10, 20, 30, 40, 50]

# Imprimir el promedio calculado o el mensaje si la lista está vacía
print("El promedio es:", calcular_promedio(lista_numeros))