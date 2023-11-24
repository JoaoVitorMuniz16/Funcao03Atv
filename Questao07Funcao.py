def item(b):
    valor_desconto = b * 0.10
    valor_final = b * 0.90
    print(valor_desconto)
    print(valor_final)
b = float(input("Digite o valor do produto:"))
item(b)