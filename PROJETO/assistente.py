import pyttsx3 
import speech_recognition as sr   
import wikipedia  
from classes import Usuario
   
def comando_fala(): 
    r = sr.Recognizer() 
    print('\nEstou a escuta.')
    with sr.Microphone() as source: audio = r.listen(source)
    r.pause_threshold = 0.8
        
    try:  
        comando = r.recognize_google(audio, language='pt') 
        print("\nO comando dito foi: ", comando) 
    except Exception as e: 
        print(e) 
        print("Frase não reconhecida, favor repetir!") 
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

def pega_comando(nome_usuario): 

    saudacao(nome_usuario) 

    while(True): 
        comando = comando_fala().lower() 
        if "pesquise" in comando or "pesquisar" in comando or "buscar" in comando or "pesquisa" in comando: 
            fala("Procurando no wikipedia sobre") 
            comando = comando.replace("pesquise", "")
            comando = comando.replace("pesquisar", "") 
            comando = comando.replace("pesquisa", "")
            comando = comando.replace("buscar", "")
            wikipedia.set_lang("pt")  
            resultado = wikipedia.summary(comando, sentences=3) 
            fala("O resultado da pesquisa foi:") 
            fala(resultado)
            continue

        #elif "atualizar" in comando or "atualize" in comando:
            #print(usuario)    
        
        elif "sair" in comando or "fechar" in comando:
            break

        else:
            fala('Desculpa! Não Entendi. Repita Por Favor!')