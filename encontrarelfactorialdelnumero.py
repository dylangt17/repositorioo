#Problema: Este código debería calcular el factorial de un número (el producto de todos los números enteros positivos hasta ese número), pero no produce el resultado correcto.


#def factorial(n):

#    resultado = 1

#    for i in range(1, n + 1):

#        resultado *= i

#    return resultado



#numero = 5

#print("Factorial de", numero, "es:", factorial(numero))
            
#Explicación: El código parece estar bien, pero asegúrate de que funcione para todos los números enteros positivos, incluidos el 0 y el 1.

#Deber: Asegúrate de que el código funcione correctamente para calcular el factorial de cualquier número entero positivo.

#Pista: Verifica cómo se inicializa y se actualiza la variable
#resultado
#en el bucle. ¿Funciona correctamente para todos los casos posibles?


def factorial(n):
    # Verificar si el número es negativo
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    
    resultado = 1
    
    # Calcular el factorial solo si n es mayor o igual a 0
    for i in range(1, n + 1):
        resultado *= i

    return resultado

numero = 5
print("Factorial de", numero, "es:", factorial(numero))

# Pruebas adicionales
print("Factorial de 0 es:", factorial(0))  # Debe ser 1
print("Factorial de 1 es:", factorial(1))  # Debe ser 1
print("Factorial de 10 es:", factorial(10))  # Verificación para un número más grande
