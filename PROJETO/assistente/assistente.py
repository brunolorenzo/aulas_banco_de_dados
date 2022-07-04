#Alunos: Bruno Lorenzo, Eduardo Peron, Enzo Salamão, Guilherme de Sá

import pyttsx3 
import speech_recognition as sr   
import wikipedia
import sqlite3
from colorama import Fore, Style
   
def comando_fala(): 
    r = sr.Recognizer() 
    print(Fore.MAGENTA +'\n  Estou a escuta.')
    print(Style.RESET_ALL)
    with sr.Microphone() as source: audio = r.listen(source)
    r.pause_threshold = 0.8
        
    try:  
        comando = r.recognize_google(audio, language='pt') 
        print("\n  O comando dito foi: ", comando) 
    except Exception as e: 
        print(e) 
        print("  Frase não reconhecida, favor repetir!") 
        return "None"
    return comando 
  
def fala(audio): 
    engine = pyttsx3.init() 
    voz = engine.getProperty('voices') 
    engine.setProperty('voice', voz[0].id) 
    engine.say(audio)   
    engine.runAndWait()      
 
def saudacao(nome_usuario): 
    fala("Seja bem-vindo ao seu assistente virtual, em que posso ajudar hoje {}?".format(nome_usuario)) 

def pega_comando(usuario): 

    nome_usuario = usuario[1][1]
    saudacao(nome_usuario) 

    while(True): 
        comando = comando_fala().lower() 
        if "pesquise" in comando or "pesquisar" in comando or "buscar" in comando or "pesquisa" in comando: 
            comando = comando.replace("pesquise", "")
            comando = comando.replace("pesquisar", "") 
            comando = comando.replace("pesquisa", "")
            comando = comando.replace("buscar", "")
            fala("Procurando no wikipedia sobre {}".format(comando))
            wikipedia.set_lang("pt")  
            resultado = wikipedia.summary(comando, sentences=3) 
            fala("O resultado da pesquisa foi:") 
            fala(resultado)
            continue

        elif "atualizar" in comando or "atualize" in comando:

            nome = input('  Digite o nome para atualizar: ')
            if nome == '':
                nome = usuario[1][1]

            idade = input('  Digite a idade para atualizar: ' )
            if idade == '':
                idade = usuario[1][2]

            email = input('  Digite o email para atualizar: ' )
            if email == '':
                email = usuario[1][3]

            senha = input('  Digite a nova senha: ' )
            if senha == '':
                senha = usuario[1][5]

            cpf = usuario[1][4]

            connection = sqlite3.connect('Usuarios.db')
            cursor = connection.cursor()
            comando_sql = """
            UPDATE Usuarios SET nome=?, idade=?, email=?, senha=? WHERE cpf = ?
            """

            cursor.execute(comando_sql, [nome, idade, email, senha, cpf])
            connection.commit()

            print(Fore.GREEN + '\n  Atualização feita com sucesso!')
            print(Style.RESET_ALL)
            connection.close() 

        elif "sair" in comando or "fechar" in comando:
            print(Fore.LIGHTYELLOW_EX + '\nFinalizando assistente ...')
            print(Style.RESET_ALL)
            break

        else:
            fala('Desculpa! Não Entendi. Repita Por Favor!')