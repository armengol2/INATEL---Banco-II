from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro
from motorista_dao import MotoristaDAO

class MotoristaCLI:
    def __init__(self):
        self.dao = MotoristaDAO()

    def menu(self):
        while True:
            print("<======== MENU ========>")
            print("1.....Criar um Motorista")
            print("2.....Listar todos os Motoristas")
            print("3.....Atualizar dados de Motorista")
            print("4.....Deletar Motorista")
            print("5.....Fechar sistema")
            opcao = input("opção---> ")

            if opcao == "1":
                self.criar_motorista()
            elif opcao == "2":
                self.listar_motoristas()
            elif opcao == "3":
                self.atualizar_motorista()
            elif opcao == "4":
                self.deletar_motorista()
            elif opcao == "5":
                print("Obrigado por escolher nossos serviços:)")
                break
            else:
                print("Opção invalida detectada")

    def criar_motorista(self):
        nome = input("Nome do motorista: ")
        cnh = input("CNH do motorista: ")

        corridas = []
        while True:
            nota = float(input("Nota da corrida: "))
            distancia = float(input("Distância em (km): "))
            valor = float(input("Valor em (R$): "))
            nome_passageiro = input("Nome do passageiro: ")
            doc_passageiro = input("Documento do passageiro: ")

            passageiro = Passageiro(nome_passageiro, doc_passageiro)
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            outra = input("Adicionar outra corrida(s/n): ").lower()
            if outra != 's':
                break

        motorista = Motorista(nome, cnh, corridas)
        self.dao.collection.insert_one(motorista.to_dict())
        print("Cadastro realizado!")

    def listar_motoristas(self):
        motoristas = self.dao.listar_motoristas()
        for m in motoristas:
            print(f"\nNome: {m['nome']}")
            print(f"CNH: {m['cnh']}")
            if 'corridas' in m:
                print("Corridas:")
                for c in m['corridas']:
                    print(f"  Nota: {c['nota']}, Distância: {c['distancia']}, Valor: {c['valor']}")
                    print(f"  Passageiro: {c['passageiro']['nome']} - {c['passageiro']['documento']}")

    def atualizar_motorista(self):
        cnh = input("CNH do motorista: ")
        novo_nome = input("Novo nome: ")
        self.dao.atualizar_motorista(cnh, novo_nome)
        print("Motorista atualizado!")

    def deletar_motorista(self):
        cnh = input("CNH do motorista: ")
        self.dao.deletar_motorista(cnh)
        print("Motorista deletado!")