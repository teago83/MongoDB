from pymongo import MongoClient
from conexao import MongoConnect
import random

cliente = MongoClient('localhost', 27017)
db = cliente.teste #nome do banco
colecao = db.aluno #nome da coleção

class Aluno():
    
    def save(self, nome, sobrenome, matricula):
        conexao = MongoConnect()
        aluno = {'nome': nome, 'sobrenome': sobrenome, 'matricula': matricula}
        conexao.save(aluno)
    
    def create(self):
        nome_create = input("Digite o nome do(a) aluno(a) a ser cadastrado(a):")
        sobrenome_create = input("Digite o sobrenome do(a) %s:" % (nome_create))
        matricula_create = 100000 + random.randint(1, 99999)
        self.save(nome_create, sobrenome_create, matricula_create)
    
    def read(self):
        op = int(input("Opções:"
                        "\n1) Ver todos os alunos cadastrados;"
                        "\n2) Pesquisar por um(a) aluno(a) específico(a) por nome;"
                        "\nDigite a opção desejada."))
        if op == 1: 
            mostrar_todos = colecao.find()
            for i in mostrar_todos:
                print(i)
        elif op == 2:
            nome_read = input("Digite o nome do(a) aluno(a) pelo(a) qual buscas:")
            query_read = {'nome': nome_read}
            mostrar_um = colecao.find(query_read)
            for i in mostrar_um:
                print(i)
    
    def update(self):
        nome_update = input("Digite o nome do(a) aluno(a) pelo(a) qual buscas:")
        sobrenome_update = input("Digite o sobrenome do(a) aluno(a) pelo(a) qual buscas:")
        a = input("Digite o novo nome do(a) %s:" % (nome_update))
        b = input("Digite o novo sobrenome do(a) %s:" % (nome_update))
        query_veio = {'nome': nome_update, 'sobrenome': sobrenome_update}
        query_novo = { "$set": {'nome': a, 'sobrenome': b} }
        colecao.update_one(query_veio, query_novo)


    def delete(self):
        nome_delete = input("Digite o nome do(a) aluno(a) pelo(a) qual buscas:")
        query_delete = {"nome": nome_delete}
        colecao.delete_one(query_delete)