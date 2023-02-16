def aumentar(n=0):
    return n + 10

def diminuir(n=0):
    return n - 15

def dobro(n=0):
    return n * 2

def metade(n=0):
    return n / 2

def moeda(preço = 0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.', ',')