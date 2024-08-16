#Problema: Este código debería verificar si un número es primo (un número mayor que 1 que solo es divisible por 1 y por sí mismo), pero está marcando números no primos como primos.


#def es_primo(n):

#    if n <= 1:

#        return False

#    for i in range(2, n):

#        if n % i == 0:

#        return False

#    return True


#numero = 29

#print(f"¿El número {numero} es primo? {es_primo(numero)}")
            
#Explicación: Este código es correcto para muchos números, pero no es eficiente. Puede ser optimizado para detenerse más temprano y evitar operaciones innecesarias.

#Deber: Optimiza el código para que se detenga cuando sea evidente que el número no es primo, en lugar de recorrer todos los números hasta
#n-1


#Pista: Puedes detener la búsqueda antes si recuerdas que no es necesario comprobar divisores mayores que la raíz cuadrada de
#n


import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Solo es necesario verificar hasta la raíz cuadrada de n
    raiz_cuadrada = int(math.sqrt(n)) + 1
    for i in range(5, raiz_cuadrada, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

numero = 29
print(f"¿El número {numero} es primo? {es_primo(numero)}")