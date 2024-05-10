# Explicación del Algoritmo de Factorial

## Introducción
Este documento ofrece una explicación detallada del método recursivo utilizado para calcular el factorial de un número entero no negativo. El factorial de un número `n`, denotado como `n!`, es el producto de todos los enteros positivos menores o iguales a `n`.

## Función Recursiva del Factorial

La función `factorial` en Python utiliza un método recursivo para calcular el factorial de un número. Este método implica que la función se llame a sí misma con valores decrecientes hasta alcanzar un caso base simple. En términos prácticos, calcular el factorial de un número significa multiplicar ese número por el factorial del número anterior a él, y así sucesivamente, hasta que se llega al número uno. La recursión es efectiva aquí porque simplifica el cálculo al descomponer un problema grande (como calcular `n!`) en problemas más pequeños y manejables (como calcular `(n-1)!`, `(n-2)!`, etc.), hasta llegar al caso más simple, que es `0! = 1`.

# Bubble Sort Explanation

## Objetivo
El objetivo de este documento es proporcionar una comprensión clara del método de ordenación Bubble Sort (Ordenamiento Burbuja), explicando su funcionamiento y demostrando su aplicación en un contexto teórico. Este documento se centra en la descripción conceptual sin la implementación de código y proporciona un script de ejemplo para ilustrar el proceso.

## Bubble Sort

### ¿Qué es Bubble Sort?
Bubble Sort, también conocido como ordenamiento burbuja, es un algoritmo de ordenación simple que itera repetidamente a través de una lista, comparando elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que no se necesitan más intercambios, lo que indica que la lista está ordenada.

### ¿Cómo funciona?
El algoritmo Bubble Sort comienza en el inicio de la lista y compara el primer elemento con el siguiente, intercambiándolos si el primero es mayor que el segundo. Continúa haciendo esto para cada par de elementos adyacentes a través de la lista. Al final de cada iteración, el siguiente elemento más grande se habrá "burbujeado" hasta su posición correcta en la lista. Con cada pasada a través de la lista, menos elementos son necesarios para ser revisados.

### ¿Cuándo es conveniente utilizar Bubble Sort?
Bubble Sort es mejor utilizar en situaciones donde:
- La simplicidad es más importante que la eficiencia.
- La lista a ordenar es relativamente pequeña o ya está parcialmente ordenada, ya que el algoritmo tiene una complejidad temporal de O(n^2) en el peor caso.
- Se requiere un algoritmo de ordenación estable que no cambie el orden relativo de elementos con claves iguales.

### Ejemplo Conceptual
Consideremos la lista de números: [34, 7, 23, 32, 5]. A continuación, se muestra cómo Bubble Sort ordenaría esta lista paso a paso:

1. **Primera Pasada:**
   - Comparar 34 y 7, como 34 > 7, intercambiar: [7, 34, 23, 32, 5]
   - Comparar 34 y 23, como 34 > 23, intercambiar: [7, 23, 34, 32, 5]
   - Comparar 34 y 32, como 34 > 32, intercambiar: [7, 23, 32, 34, 5]
   - Comparar 34 y 5, como 34 > 5, intercambiar: [7, 23, 32, 5, 34]

2. **Segunda Pasada:**
   - Comparar 7 y 23, no intercambiar: [7, 23, 32, 5, 34]
   - Comparar 23 y 32, no intercambiar: [7, 23, 32, 5, 34]
   - Comparar 32 y 5, como 32 > 5, intercambiar: [7, 23, 5, 32, 34]

3. **Tercera Pasada:**
   - Comparar 7 y 23, no intercambiar: [7, 23, 5, 32, 34]
   - Comparar 23 y 5, como 23 > 5, intercambiar: [7, 5, 23, 32, 34]

4. **Cuarta Pasada:**
   - Comparar 7 y 5, como 7 > 5, intercambiar: [5, 7, 23, 32, 34]

Después de estos pasos, la lista está completamente ordenada: [5, 7, 23, 32, 34].
