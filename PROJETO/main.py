#Alunos: Bruno Lorenzo, Eduardo Peron, Enzo Salamão, Guilherme de Sá

from classe.classe_dao import UsuarioDAO
from colorama import Fore, Style
from banco_de_dados import utils
from banco_de_dados import criar_bd
import os

if __name__ == '__main__':
    
    bd_path = 'Usuarios.db'
    
    if not os.path.exists(bd_path):
        criar_bd.criar_bd_usuario(bd_path)

    usuario_dao = UsuarioDAO(bd_path)

    while True:

        print('\n\n---------------- Menu -----------------')

        print('\n  1 – Fazer Login')
        print('  2 – Recuperar Senha')
        print('  3 – Novo Usuário')
        print('  4 – Sair')

        opcao = input('\nDigite a opção desejada: ')

        if opcao == '1':
            utils.login_usuario(usuario_dao)
        elif opcao == '2':
            utils.recuperar_senha(usuario_dao)
        elif opcao == '3':
            print('\n\n  Opção 3')
            utils.cadastrar_usuario(usuario_dao)
        elif opcao == '4':
            break
        else:
            print(Fore.RED + '\n  Opção Inválida!') 
            print(Style.RESET_ALL)

    print(Fore.LIGHTYELLOW_EX + '\n  Sistema Finalizado ...')
    print(Style.RESET_ALL)