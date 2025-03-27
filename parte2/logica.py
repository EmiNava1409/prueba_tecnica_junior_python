def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def analizar_texto(texto):
    palabras = texto.split()

    letras = sum(len(''.join(c for c in palabra if c.isalpha()))
    for palabra in palabras)
    return {'palabras': len(palabras), 'letras': letras}

texto = "Hola Emilia Avila"
print(analizar_texto(texto))
