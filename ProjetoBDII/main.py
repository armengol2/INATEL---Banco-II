from pymongo import MongoClient
from Clientes import ClientesModel
from ContatoCliente import ContatoCliente
from datetime import datetime

#================================ CONEXÃO COM O BANCO ============================================
client = MongoClient("mongodb://localhost:27017/")
db = client["BancoFocus"]
clientes_model = ClientesModel(db)

#================================== ÁREA DO MENU =================================================
def menu():
    print("============================================== ™FOCUS =======================================================")
    print("------- MENU -------")
    print("1-> Cadastrar")
    print("2-> Buscar cadastro")
    print("3-> Atualizar cadastro")
    print("4-> Processo Finalizado")
    print("5-> Clientes do mês")
    print("6-> Sair")

while True:
    menu()
    opcao = input("Insira um número ---->")

#================================== CASE 1 - CADASTRO =================================================
    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        try:
            dia = int(input("Dia da entrevista (dd): "))
            mes = int(input("Mês da entrevista (mm): "))
            hora = int(input("Hora da entrevista (24h): "))
            data_entrevista = datetime(2025, mes, dia, hora, 0)
            contato = ContatoCliente(email, telefone)
            clientes_model.create_cliente(nome, contato, data_entrevista)
        except Exception as e:
            print("Erro ao registrar data.")

#================================== CASE 2 - BUSCA =================================================
    elif opcao == "2":
        nome_cliente = input("Nome completo: ")
        clientes_model.read_cliente_by_nome(nome_cliente)

#================================== CASE 3 - ATUALIZAÇÃO =================================================
    elif opcao == "3":
        id_cliente = input("ID para atualizar: ")
        campo = input("Qual campo deseja atualizar?(nome, email, telefone, data): ").lower()
        if campo == "data":
            try:
                dia = int(input("Novo dia: "))
                mes = int(input("Novo mês: "))
                hora = int(input("Nova hora: "))
                nova_data = datetime(2025, mes, dia, hora, 0)
                clientes_model.update_cliente(id_cliente, {"data_entrevista": nova_data})
            except:
                print("Data inválida.")
        elif campo in ["email", "telefone"]:
            novo_valor = input(f"Novo valor para {campo}: ")
            clientes_model.update_cliente(id_cliente, {campo: novo_valor})
        elif campo == "nome":
            novo_valor = input(f"Novo valor para {campo}: ")
            clientes_model.update_cliente(id_cliente, {"nome": novo_valor})
        else:
            print("Campo inválido.")

#================================== CASE 4 - REMOÇÃO =================================================
    elif opcao == "4":
        id_cliente = input("ID para deletar: ")
        clientes_model.delete_cliente(id_cliente)

#================================== CASE 5 - BUSCA COMPLETA =================================================
    elif opcao == "5":
        try:
            ano = int(input("Digite o ano: "))
            mes = int(input("Digite o mês(númerico): "))
            clientes_model.read_clientes_por_mes(ano, mes)
        except ValueError:
            print("Ano / mês inconclusivos.")

#================================== CASE 6 - SAÍDA =================================================
    elif opcao == "6":
        print("Have a nice day;)")
        break

    else:
        print("Opção inconclusiva.")