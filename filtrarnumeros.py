#Problema: El siguiente código debería filtrar solo los números pares de una lista, pero no está funcionando correctamente.


#def filtrar_pares(numeros):

#    pares = []

 #   for numero in numeros:

  #      if numero % 2 == 0:

   #         pares.append(numero)

    #return pares



#lista_numeros = [1, 2, 3, 4, 5, 6]

#print("Números pares:", filtrar_pares(lista_numeros))
            
#Explicación: El código parece estar bien, pero hay un error en la lógica que podrías no notar a primera vista. Debes verificar si realmente está filtrando todos los números pares.

#Deber: Asegúrate de que el código funciona correctamente para listas con números positivos, negativos e incluso con ceros.

#Pista: ¿Qué pasa con números negativos y el cero? Recuerda que el operador

#se comporta de manera predecible con cualquier número entero.


def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Lista de números que incluye positivos, negativos y cero
lista_numeros = [1, 2, 3, 4, 5, 6, -2, -4, 0]

# Imprimir los números pares filtrados
print("Números pares:", filtrar_pares(lista_numeros))