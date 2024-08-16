#Problema: Este código debería encontrar el valor máximo en una lista de números, pero devuelve resultados incorrectos.


#def encontrar_maximo(numeros):

 #   maximo = 0

  #  for numero in numeros:

   #     if numero > maximo:

    #        maximo = numero

    #return maximo


#lista_numeros = [-10, -20, -30, -5, -15]

#print("El valor máximo es:", encontrar_maximo(lista_numeros))
            
#Explicación: El error aquí es que el valor inicial de
#maximo
#está incorrectamente configurado para manejar listas que contienen solo números negativos. ¿Cómo puedes corregirlo?

#Deber: Modifica el código para que funcione con cualquier lista, incluyendo listas con solo números negativos.

#Pista: Piensa en cuál debería ser el valor inicial de
#maximo
#para manejar listas con números negativos.


def encontrar_maximo(numeros):
    # Verificar si la lista está vacía
    if len(numeros) == 0:
        return "La lista está vacía"
    
    # Inicializar maximo al primer elemento de la lista
    maximo = numeros[0]

    for numero in numeros:
        if numero > maximo:
            maximo = numero

    return maximo

lista_numeros = [-10, -20, -30, -5, -15]

print("El valor máximo es:", encontrar_maximo(lista_numeros))