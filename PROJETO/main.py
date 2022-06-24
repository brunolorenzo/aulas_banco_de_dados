from assistente import pega_comando
from classes import Usuario
lista = []
lista_cpf = []
lista_email = []
nome = 'bruno'
CPF = '123'
email_= 'lorenzo'
idade = '60'
senha = '456'

usuarios = Usuario(nome, idade, email_, CPF, senha)
lista.append(usuarios)
while(True):

    opcao = input("\n-------------- Menu Principal --------------\n\n1 - Fazer Login\n2 - Recuperar Senha\n3 - Novo Usuário\n4 – Sair\n\nOpção: ")

    if opcao == '1':
        
        cpf = input("Digite o seu cpf: ")
        for k in range(len(lista)):
            if cpf == lista[k]._cpf:
                senha = input("Digite a sua senha: ")
                if senha == lista[k]._senha:
                    print('\nLogin efetuado com sucesso!')
                    pega_comando(lista[k]._nome)
                else:
                    print("\nSenha incorreta!")

            elif k == len(lista)-1:
                print('\nCPF invalido')

    #elif opcao == 2:
    #    pass

    elif opcao == '3':
        # nome = input('Digite o nome: ')
        # CPF = input('Digite o CPF: ')
        # email_ = input('Digite o email: ')
        # idade = input('Digite a idade: ')
        # senha = input('Digite a senha: ')
        nome = 'guilherme'
        CPF = '333'
        email_= '898'
        idade = '20'
        senha = '789'



        usuarios = Usuario(nome, idade, email_, CPF, senha)
        lista.append(usuarios)
        print(usuarios._nome)

    elif opcao == '4':
        break

    else:
        print('\nCódigo inválido, digite novamente!')
        continue
