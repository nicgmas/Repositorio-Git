'''Escreva uma função chamada classificar_nota
que recebe uma nota e retorna "Aprovado",
"Reprovado" ou "Em Recuperação" com base na nota.'''

def classificar_nota(nota):
    
    if nota >= 7:
        return "Aprovado"
    
    elif nota >= 6:
        return "Em Recuperação"

    
    else :
        return "Aluno(a) Reprovado(a)"
    
print(classificar_nota(8))