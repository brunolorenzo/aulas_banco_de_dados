#Alunos: Bruno Lorenzo, Eduardo Peron, Enzo Salamão, Guilherme de Sá

from assistente import assistente
from classe.classe import Usuario
from colorama import Fore, Style
from random import choice
import email.message
import sqlite3
import string
import smtplib

def cadastrar_usuario(usuario_dao):
    
    print(Fore.BLUE + '\n\n------------- Cadastro de Usuário --------------')
    print(Style.RESET_ALL)

    cpf = input('\n\n  CPF: ')
    
    usuario_existente = usuario_dao.buscar_cpf(cpf)

    if usuario_existente is not None:        
        print(Fore.RED + '  Já existe um usuário cadastrado com o CPF digitado Digitado!')
        print(Style.RESET_ALL)
        return

    nome = input('  Nome: ')
    
    idade = int(input('  Idade: '))

    email = input('  Email: ')

    senha = input('  Senha: ')

    usuario_insert = Usuario(nome, idade, email, cpf, senha)

    insert_ok = usuario_dao.inserir_usuario(usuario_insert)

    if insert_ok:
        print(Fore.GREEN + '\n\nUsuário Cadastrado com Sucesso!')
    else:
        print(Fore.RED + '\n\nErro no Cadastrado!')

    print(Style.RESET_ALL)

def login_usuario(usuario_dao):

    print(Fore.BLUE + '\n\n------------- LOGIN --------------')
    print(Style.RESET_ALL)

    cpf = input('\n\n  CPF: ')
    
    usuario_existente = usuario_dao.buscar_cpf(cpf)

    if usuario_existente is not None:
        senha = input('  Senha: ')

        if senha == usuario_existente[1][5]:
            print(Fore. GREEN + '  Login efetuado com Sucesso!')
            print(Style.RESET_ALL)
            assistente.pega_comando(usuario_existente)
        
        else:
            print(Fore.RED + '\n  Senha Incorreta!')
            print(Fore.WHITE + '  Voltando para o menu inicial.')
            print(Style.RESET_ALL)

        return

    else:
        print(Fore.RED + '\n  CPF Inválido!')
        print(Fore.WHITE + '  Voltando para o menu inicial.')
        print(Style.RESET_ALL)

def recuperar_senha(usuario_dao):

    senha = gerar_senha()

    print(Fore.BLUE + '\n\n------------- RECUPERAR SENHA --------------')
    print(Style.RESET_ALL)
    
    email_usuario = input('\n\n  Digite o email para recuperar senha: ')
    
    usuario_existente = usuario_dao.buscar_email(email_usuario)

    if usuario_existente is not None:

        corpo_email = 'Oi {}, sua nova senha é {}'.format(usuario_existente[1][1], senha)
        
        msg = email.message.Message()
        msg['Subject'] = 'RECUEPERAÇÃO SENHA'
        msg['From'] = 'br12kl34bruno@gmail.com'
        msg['To'] = email_usuario
        password = "ipbrrxvchkxylabv"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        connection = sqlite3.connect('Usuarios.db')
        cursor = connection.cursor()
        comando_sql = """
        UPDATE Usuarios SET senha=? WHERE email = ?
        """
        cursor.execute(comando_sql, [senha, email_usuario])
        connection.commit()

        print(Fore.GREEN + '\n  Senha enviada com Sucesso!')
        print(Style.RESET_ALL)
        connection.close() 
        return

    else:
        print(Fore.RED + '\n  EMAIL Inválido!')
        print(Fore.WHITE + '  Voltando para o menu inicial.')
        print(Style.RESET_ALL)

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_gerada = ''
    for i in range(5):
        senha_gerada += choice(caracteres)
    
    return senha_gerada

def enviar_email(): 
    corpo_email = 'Olá'

    msg = email.message.Message()
    msg['Subject'] = 'RECUEPERAÇÃO SENHA'
    msg['From'] = 'br12kl34bruno@gmail.com'
    msg['To'] = 'enzosalamaoroseiro@gmail.com'
    password = "ipbrrxvchkxylabv"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')