
#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

c = 4

qtdObesos = 0

i = 0

while c > 0:
    iDoNoia = int(input(""))
    pesoDoNoia = float(input(""))

    if pesoDoNoia > 90:
        qtdObesos = qtdObesos + 1
        i = i + iDoNoia
        c = c - 1 

    else:
        i = i + iDoNoia
        c = c - 1

media = i / 4
print("Qtd pessoas > 90 Kg: %i" %(qtdObesos))
print("Idade média: %.2f" %(media))