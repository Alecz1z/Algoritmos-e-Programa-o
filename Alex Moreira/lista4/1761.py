#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761


sc = 0
t = 0
while True:
    n1 = float(input(''))
    if n1 == 0:
        n2 = float(input(''))
        t = n2 - sc
        break
    else:
        sc = sc + n1
print("Total da compra: R$%.2f"%(sc))
print("Valor pago: R$%.2f"%(n2))
print("Troco: R$%.2f"%(t))