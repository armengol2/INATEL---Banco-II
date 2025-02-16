from Professor import Professor
from Aluno import Aluno

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        presenca_str = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:"
        for aluno in self.alunos:
            presenca_str += f"\n{aluno.presenca()}"
        return presenca_str