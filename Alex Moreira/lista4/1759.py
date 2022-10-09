#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

aat = int(input())

vi = 1015

a = aat - 2006

valorSomado = 1015

contadorPorcentagem = 0.015 

somaPorcentagem = 0.01

if aat < 2006:
    print("O ano informado deverá ser > 2005!")

elif aat == 2006:
    print("Salário atual: R$%.2f"%(vi))
    
 

elif aat > 2006:
    porcentagem = (0.015 + 0.01)
    aat = vi

    for i in range(a):
        calculo = aat + (aat * porcentagem)
        aat = calculo
        porcentagem = porcentagem + 0.01

        
    print("Salário atual: R$%.2f"%(calculo))



    