from pymongo import MongoClient
#pip install pymongo

class MongoConnect():

    def save(self, json):
        try:
            cliente = MongoClient('localhost', 27017)
            db = cliente.teste #nome do banco
            colecao = db.aluno #nome da coleção
            id = colecao.insert_one(json).inserted_id
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)