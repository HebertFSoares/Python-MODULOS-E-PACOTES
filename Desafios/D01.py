import moeda
num = float(input("Digite um valor: "))
m = moeda.aumentar(num)
d = moeda.dobro(num)
di = moeda.diminuir(num)
me = moeda.metade(num)
'''
print(f"Aumentando mais R$10.00 do seu valor, Preço Final R${m}.00")
print(f"Dobrando seu valor R${num}.00, Preço Final R${d}.00")
print(f"Diminuindo R$15.00 do seu valor, Preço Final R${di}.00")
print(f"A metade do seu valor R${num}.00, Preço Final R${me}")

'''
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(num)}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}")
