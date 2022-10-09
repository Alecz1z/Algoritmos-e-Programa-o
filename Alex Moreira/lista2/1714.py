#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

pc = float(input())

if  pc < 20.00: 
    valorProduto = pc * 0.45 + pc
    print("Valor de venda: R$%.2f" %valorProduto)

else:
    valorProduto2 = pc * 0.30 + pc
    print("Valor de venda: R$%.2f" %valorProduto2)