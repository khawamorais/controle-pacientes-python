pacientes = []

def adicionar():
    nome = input("Digite o nome do paciente: ")
    pacientes.append(nome)
    print("Paciente adicionado com sucesso!")

def listar():
    print("\nLista de pacientes:")
    for p in pacientes:
        print("-", p)

def buscar():
    nome = input("Digite o nome para buscar: ")
    if nome in pacientes:
        print("Paciente encontrado!")
    else:
        print("Paciente não encontrado.")

def remover():
    nome = input("Digite o nome para remover: ")
    if nome in pacientes:
        pacientes.remove(nome)
        print("Paciente removido.")
    else:
        print("Paciente não encontrado.")

def menu():
    while True:
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Remover")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "3":
            buscar()
        elif op == "4":
            remover()
        elif op == "0":
            break
        else:
            print("Opção inválida")

menu()
