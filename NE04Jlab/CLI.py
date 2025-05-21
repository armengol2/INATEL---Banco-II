from database import Database
from teacherCRUD import TeacherCRUD


class CLI:
    def __init__(self, crud):
        self.crud = crud

    #menu de seleção de opção
    def menu(self):
        while True:
            print("\n------ INATEL:Professores ------")
            print("1 -> Criar professor")
            print("2 -> Ler professor")
            print("3 -> Atualizar CPF")
            print("4 -> Deletar professor")
            print("5 -> Saindo")
            opcao = input("Escolha: ")
            #Inserindo professores ao BD
            if opcao == "1":
                name = input("Nome: ")
                ano = int(input("Ano de nascimento: "))
                cpf = input("CPF: ")
                self.crud.create(name, ano, cpf)
                print("Professor cadastrado.")
            #Lendo informações do professor
            elif opcao == "2":
                name = input("Nome: ")
                res = self.crud.read(name)
                if res:
                    print("Nome:", res["name"])
                    print("Ano de nascimento:", res["ano_nasc"])
                    print("CPF:", res["cpf"])
                else:
                    print("Professor não encontrado")
            #Atualizando o CPF
            elif opcao == "3":
                name = input("Nome: ")
                newCpf = input("Novo CPF: ")
                self.crud.update(name, newCpf)
                print("CPF atualizado.")
            #Deletendo professores
            elif opcao == "4":
                name = input("Nome: ")
                self.crud.delete(name)
                print("Professor deletado.")
            #Saindo do sistema
            elif opcao == "5":
                print("Desligando sistema...")
                break

            else:
                print("Opção inválida.")

    @staticmethod
    def run():
        db = Database("bolt://localhost:7687", "neo4j", "neo4jneo4j")
        crud = TeacherCRUD(db)
        app = CLI(crud)
        try:
            app.menu()
        finally:
            db.close()


if __name__ == "__main__":
    CLI.run()