from abc import ABC, abstractclassmethod
# from <módulo> import <nome>
# módulo: nome do módulo ou pacote que você irá importar
#nome: nome da função , classe, variável ou sbmódulo que deseja importar
#import React from "react" ;

'''Classe abstrata: classe que não pode ser instanciada diretamente(não consigo criar)
 objetos diretamente nela. Definimos regras que devem ser obedecidas'''

class Curso(ABC):
    def _init_(self,nome):
        self.nome = nome
        self.alunos = []

    def inscrever_alunos(self,aluno,matricula):
        self.alunos.append(aluno, matricula)
        print(f"Aluno {aluno} com matricula nº {matricula}, inscrito no curso {self.nome} .")

    @abstractclassmethod
    def info_curso(self):
        pass

def info_alunos(self):
    print(f"Alunos inscritos no curso{self.nome}:")
    for aluno,matricula  in self.alunos:
        print(f" -Nome: {aluno}, Matrícula: {matricula}")

class CursoMatematica(Curso):
    def info_curso(self):
        print(f"Curso de {self.nome} : Foco em álgebra e geometria")

#Curso específico
class CursoHistoria (Curso):
    def info_curso(self):
        print(f"Curso de {self.nome} : Foco em história mundial e cultura")


#testar
curso1 = CursoMatematica("Matemática")
curso2 = CursoHistoria("História")

curso1.inscrever_alunos("Breno","RES12351123")
curso1.inscrever_alunos("Rayssa","RES1304815")
curso1.info_curso()
curso1.info_alunos()

curso2.inscrever_alunos("Ágatha", "RES")
curso2.info_curso()

#crie a função info_alunos()
curso1.info_alunos()
curso2.info_alunos()

#inserir matrícula
    

    