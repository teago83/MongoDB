from aluno import Aluno
pedro = Aluno()
op = 0

class Menu():
    def menu(self):
        op = 6
        while op > 5 or op < 1:
            op = int(input("Menu de opções:\n1) Registrar novo(a) aluno(a);\n2) Procurar por/pesquisar aluno(a);\n3) Atualizar aluno(a);\n4) Deletar aluno(a);\n5) Sair.\nDigite a opção desejada."))
            if op == 1:
                pedro.create()
            elif op == 2:
                pedro.read()
            elif op == 3:
                pedro.update()
            elif op == 4:
                pedro.delete()
            elif op == 5:
                exit()

cassio = Menu()
while op != 5:
    cassio.menu()