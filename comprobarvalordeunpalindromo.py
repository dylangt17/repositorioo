#Problema: Este código debería comprobar si una palabra es un palíndromo (una palabra que se lee igual de adelante hacia atrás), pero no está funcionando correctamente para ciertas palabras.


#def es_palindromo(palabra):

#    palabra_invertida = ""

#    for i in range(len(palabra)):

#        palabra_invertida += palabra[i-1]

#    return palabra == palabra_invertida



#palabra = "radar"

#print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")
            
#Explicación: El problema radica en cómo se está construyendo la cadena invertida. Debes ajustar el código para que compare correctamente la palabra original con su versión invertida.

#Deber: Corrige el código para que pueda identificar correctamente si una palabra es un palíndromo.

#Pista: Revisa cómo se accede a los caracteres de la cadena. ¿Cómo puedes invertir correctamente la palabra?


def es_palindromo(palabra):
    palabra_invertida = ""
    # Construir la palabra invertida accediendo a los caracteres desde el final
    for i in range(len(palabra)):
        palabra_invertida += palabra[len(palabra) - 1 - i]
    return palabra == palabra_invertida

palabra = "radar"
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")