def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    result = 1
    for elemento in lista:
        result *= elemento
    return result

def calcular(**kwargs):
    for nombre, valor in kwargs.items():
        if nombre.startswith('fact_'):
            n = int(valor)
            resultado = factorial(n)
            print(f"El factorial de {n} es {resultado}")
        elif nombre.startswith('prod_'):
            lista = valor
            resultado = productoria(lista)
            print(f"La productoria de {lista} es {resultado}")

if __name__ == "__main__":
    # Ejemplos de uso
    calcular(fact_1='5', prod_2=[4, 6, 7, 4, 3],  fact_2='6')
 
