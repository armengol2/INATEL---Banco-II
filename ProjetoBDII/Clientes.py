import smtplib
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from email.message import EmailMessage
from ContatoCliente import ContatoCliente

# =================================== CONFIGURAÇÃO DE EMAIL ========================================
EMAIL_ORIGEM = 'rodrigoarmengol2@gmail.com'
SENHA = 'xxxxxxxxxxxxxxxxxxx'
EMAIL_DESTINO = 'rodrigoarmengol2@gmail.com'

def enviar_email(conteudo, destino):
    try:
        msg = EmailMessage()
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = destino
        msg['Subject'] = '🔔 Lembrete de Entrevista'
        msg.set_content(conteudo, charset='utf-8')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(EMAIL_ORIGEM, SENHA)
            servidor.send_message(msg)

        print("✅ Email de lembrete enviado com sucesso!")
    except Exception as e:
        print(f"Erro:( : {e}")

# ======================================= CLASSE PRINCIPAL =================================
class ClientesModel:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.Clientes

# ======================================= FUNÇÃO DE CADASTRO =================================
    def create_cliente(self, nome: str, contato: ContatoCliente, data_entrevista: datetime):
        try:
            res = self.collection.insert_one({
                "nome": nome,
                "email": contato.email,
                "telefone": contato.telefone,
                "data_entrevista": data_entrevista
            })
            print(f"Cliente criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o cliente: {e}")
            return None
# ======================================= FUNÇÃO DE ENCONTRAR CLIENTE =================================
    def read_cliente_by_nome(self, nome: str):
        try:
            res = self.collection.find_one({"nome": {"$regex": f"^{nome}$", "$options": "i"}})
            if res:
                print("Cliente encontrado:")
                print(f"ID: {res['_id']}")
                print(f"Nome: {res['nome']}")
                print(f"Email: {res['email']}")
                print(f"Telefone: {res['telefone']}")
                if isinstance(res['data_entrevista'], datetime):
                    print("Entrevista marcada para:", res['data_entrevista'].strftime("%d/%m às %Hh"))
                else:
                    print("Data da entrevista (formato inválido)")
            else:
                print(f"Nenhum cliente encontrado com o nome '{nome}'")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar cliente por nome: {e}")
            return None

# ======================================= FUNÇÃO DE ATUALIAÇÕES DA DADOS =================================
    def update_cliente(self, id: str, novos_dados: dict):
        try:
            res = self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": novos_dados}
            )
            print(f"Cliente atualizado: {res.modified_count} Modificado")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o cliente: {e}")
            return None

# ======================================= FUNÇÃO DE DELETE =================================
    def delete_cliente(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"Cliente deletado")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o cliente: {e}")
            return None

# ======================================= FUNÇÃO DE ACHAR CLIENTES COM BASE NO DIA =================================
    def read_clientes_por_mes(self, ano: int, mes: int):
        try:
            inicio = datetime(ano, mes, 1)
            fim = datetime(ano + 1, 1, 1) if mes == 12 else datetime(ano, mes + 1, 1)

            resultados = self.collection.find({
                "data_entrevista": {
                    "$gte": inicio,
                    "$lt": fim
                }
            })

            lista = list(resultados)
            if lista:
                print(f"\nClientes com entrevista marcada em {mes:02}/{ano}:")
                for c in lista:
                    print("-" * 30)
                    print(f"ID: {c['_id']}")
                    print(f"Nome: {c['nome']}")
                    print(f"Email: {c['email']}")
                    print(f"Telefone: {c['telefone']}")
                    if isinstance(c['data_entrevista'], datetime):
                        print("Entrevista:", c['data_entrevista'].strftime("%d/%m às %Hh"))
            else:
                print(f"\nNenhum cliente com entrevista marcada em {mes:02}/{ano}.")
            return lista
        except Exception as e:
            print(f"Erro ao buscar clientes por mês: {e}")
            return []

# ======================================= FUNÇÃO DE AVISO DE ENTREVISTAS =================================
    def avisar_entrevistas_atuais(self):
        agora = datetime.now()
        um_dia_depois = agora + timedelta(days=1)

        entrevistas = self.collection.find()
        avisados = False

        for cliente in entrevistas:
            data = cliente.get("data_entrevista")
            if data and isinstance(data, datetime):
                if data.date() == um_dia_depois.date():
                    conteudo = (
                        f"Cliente: {cliente['nome']}\n"
                        f": {data.strftime('%d/%m às %H:%M')}"
                    )

                    print("LEMBRETE DE ENTREVISTA")
                    print(conteudo)
                    enviar_email(conteudo, EMAIL_DESTINO)
                    avisados = True

        if not avisados:
            print(f"Sem entrevistas agendadas para amanhã ({um_dia_depois.strftime('%d/%m')})")
