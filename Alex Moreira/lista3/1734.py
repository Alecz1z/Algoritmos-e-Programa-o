#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input("") )

nmr = n

resultado=1
count=1

while count <= n:
    resultado *= count
    count += 1

print("%i ! = %i" %(nmr, resultado))