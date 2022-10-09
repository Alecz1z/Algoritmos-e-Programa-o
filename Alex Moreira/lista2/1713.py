#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
h = float(input())
nh = float(input())

total = h * nh
imposto = (total * 0.11)
inss = (total * 0.08 )
sd = (total * 0.05)
tf = total - imposto - inss - sd


print ("Salário bruto: R$%.2f" %total)
print ("Imposto: R$%.2f" %imposto)
print ("INSS: R$%.2f" %inss)
print ("Sindicato: R$%.2f" %sd)
print ("Líquido: R$%.2f " %tf)