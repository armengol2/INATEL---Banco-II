from Professor import Professor
from Aluno import Aluno
from Aula import Aula

def main():
    prof = Professor("Luis felipe")
    aluno1 = Aluno("Rodrigo")
    aluno2 = Aluno("Thiago")
    
    aula = Aula(prof, "Calculo 3")
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    
    print(prof.ministrar_aula("Calculo 3"))
    print(aula.listar_presenca())

if __name__ == "__main__":
    main()