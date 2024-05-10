def factorial(n):
    """
    Calcula el factorial de un número dado utilizando una función recursiva.

    Parameters
    ----------
    n : int
        Número entero no negativo al que se le calculará el factorial.

    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    # Caso base: si n es 0, el factorial es 1
    if n == 0:
        return 1
    # Paso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

def main():
    print("=================================================================")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
