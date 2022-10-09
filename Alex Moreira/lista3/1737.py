#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qtn = int(input(""))
va = 0 

if qtn <=0:
    print("Informe uma quantidade >0!")

else:
    while qtn > 0:
        nmr = float(input(""))
        va = va + nmr 
        qtn = qtn - 1
    print("Soma dos números informados: %.2f" %(va)) 