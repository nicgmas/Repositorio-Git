'''Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com valores
inteiros. Seu programa tme que analisar todos os valores e dizer
qual deles é o maior'''

def maior(primeiro, *restantes ):
   return max (primeiro, *restantes)

#Exemplos de uso:
print(maior(10,4,7 ,22,13,17))
print(maior(5,5,5))
