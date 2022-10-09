#https://www.beecrowd.com.br/judge/pt/problems/view/1019

s = int(input())
m = int(s/60)
s -= m*60
h = int(m/60)
m -= h*60

print(f'{h}:{m}:{s}')