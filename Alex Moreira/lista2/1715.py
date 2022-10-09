#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

cf = input()
salarioAtual = float(input())


if cf == "A":
    soma1 = 0.10 * salarioAtual + salarioAtual
    print("Novo salário: R$%.2f" %soma1)

elif cf == "B":
    soma2 = 0.15 * salarioAtual + salarioAtual 
    print("Novo salário: R$%.2f" %soma2)

elif cf == "C":

    soma3 = 0.20 * salarioAtual + salarioAtual
    print("Novo salário: R$%.2f" %soma3)
