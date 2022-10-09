#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

sm = 1192.40

vhe = 10.00



nome = input("")

he = float(input(""))




she = he * vhe

sb = 3 * sm + she







if sb > 2000:



    if sb >2500:

        descontoImpostoRenda20 = 0.20 * sb

        descontoInss = 0.12 * sb

        sl = sb - descontoInss - descontoImpostoRenda20

    else:

        descontoInss = 0.12 * sb

        sl = sb - descontoInss




else:

    descontoInss = 0.05 * sb

    sl = sb - descontoInss


print("Nome: %s" %(nome))

print("Salário Bruto: R$%.2f" %sb)

print("Salário líquido: R$%.2f" %sl)