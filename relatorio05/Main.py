from pymongo import MongoClient
from bson.objectid import ObjectId
from LivrosModel import LivrosModel

class Main:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client.biblioteca
        self.livros_model = LivrosModel(self.db)

    def run(self):
        while True:
            print("\nMenu Biblioteca:")
            print("Digite 1-> Cadastrar Livro")
            print("Digite 2-> Encontrar Livro")
            print("Digite 3-> Atualizar Livro")
            print("Digite 4-> Deletar Livro")
            print("Digite 5-> Sair")

            choice = input("Número escolhido: ")

            if choice == "1":
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = int(input("Ano de publicação: "))
                preco = float(input("Preço do livro: "))
                try:
                    res = self.livros_model.create_livro(titulo, autor, ano, preco)
                    if res:
                        print(f"Cadastro completo...ID: {res}")
                except Exception as e:
                    print(f"Informacoes invalidas ao cadastrar livro: {e}")

            elif choice == "2":
                livro_id = input("Digite o ID do livro para leitura: ")
                try:
                    res = self.livros_model.read_livro_by_id(livro_id)
                    if not res:
                        print("Nenhum livro encontrado com esse ID.")
                except Exception as e:
                    print(f"Informacoes invalidas ao buscar o livro: {e}")

            elif choice == "3":
                livro_id = input("ID do livro para atualizar: ")
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = int(input("Ano de publicação: "))
                preco = float(input("Preço do livro: "))
                try:
                    res = self.livros_model.update_livro(livro_id, titulo, autor, ano, preco)
                    if res:
                        print("Livro atualizado com sucesso")
                except Exception as e:
                    print(f"Ocorreu um erro ao atualizar o livro: {e}")

            elif choice == "4":
                livro_id = input("ID do livro para deletar: ")
                try:
                    res = self.livros_model.delete_livro(livro_id)
                    if res:
                        print("Livro deletado do banco de dados")
                except Exception as e:
                    print(f"Ocorreu um erro ao deletar o livro: {e}")

            elif choice == "5":
                print("Obrigado e até mais :)")
                break

            else:
                print("!Erro, opcão inválida!")

if __name__ == "__main__":
    main_program = Main()
    main_program.run()