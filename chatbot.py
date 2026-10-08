print("ao escrever barra conversa vai mostras as palavras que funciona")
import time
import sys
while True:
    i = input("digite: ").lower().strip()
    if i == "oi":
        print("oi tudo bem?")
    elif i == "voce conhece o planeta terra?":
        print("eu nao conheço pois sou linhas de codigos de linguagem python ")
    elif i == "como esta?":
        print("oi")
    elif i == "como voce esta?":
         print("infelismente nao tenho sentimentos pois sou apenas linha de codigos")
    elif i == "encerrar":
         print("encerrando...")
         sys.exit()
    elif i == "quem e voce?":
         print("eu sou apenas uma linha de codigos")
    elif i == "qual e o seu sonho?":
         print("infelismente nao tenho celebro para ter sonhos eu eu queria ter sonhos")         
    elif i == "voce sabe matematica?":
         print("eu nao fui feito para fazer matematicas eu fui feito para interagir")
    elif  i == "barra conversa":
             print("oi")
             print("voce conhece o planeta terra?")
             print("qual e o seu sonho?")
             print("voce sabe matematica?")
             print("quem e voce?")
             print("encerrar")
             print("como voce esta?")
             print("como esta?")
             print("qual e o seu proposito?")
             print("voce tem sentimentos?")
             print("hoje vai chover?")
             print("como voce funciona?")
             print("nome do arquivo")
             print("voce e homem?")
             print("voce e mulher?")
             print("voce existe?")
             print("joao batista")
             print("voce tem conciencia?")
             print("qual e a escola que joao batista estava em 2026?")
             print("quantos anos joao batista tinha?")
             print("voce gosta de futebol?")
             print("                                          ")
             print("> modo abaixo  <")
             print("                                          ")
             print("modo matematica")
             print("                                          ")
    elif i == "voce tem sentimentos?":
             print("nao eu nao sinto sentimentos pois so apenas linhas de codigos...")
    elif i == "hoje vai chover?":
         print("desculpe mas nao sei pois sou apenas linhas de codigos...")
    elif i == "qual e o seu proposito?":
         print("o meu proposito e apenas interagir")
    elif i == "modo matematica":
         print("escolha e digite: \n mais , menos , vezes , divisao")
         sn = input("digite um deles: ")
         print("digite somente numeros")
         e = float(input("primeiro numero"))
         h = float(input("segundo numero"))
         
         if sn == "mais":
             mais = e + h
             time.sleep(0.5)
             print(" ")
             print("resultado: ", mais)             
             time.sleep(0.2)
             print(" ")
             print("voltando...")
             time.sleep(0.2)
             print("")
             
         elif sn == "menos":
             hd = e - h
             time.sleep(0.5)
             print(" ")
             print("resultado: ", hd)             
             time.sleep(0.2)
             print(" ")
             print("voltando...")
             time.sleep(0.5)
             print("")
             
         elif sn == "vezes":
             dns = e * h
             time.sleep(0.5)
             print(" ")
             print("resultado: ", dns)
             time.sleep(0.2)
             print(" ")
             print("voltando...")
             time.sleep(0.2)
             print(" ")
             
         elif sn == "divisao":
             wwd = e / h
             time.sleep(0.2)
             print(" ")
             print("resultado da divisao: ", wwd)
             time.sleep(0.2)
             print(" ")
             print("voltando...")
             time.sleep(1)
             print(" ")
             
         else:
             print("invalido...")
             time.sleep(0.2)
             print(" ")
             print("voltando...")
             time.sleep(1)
             print(" ")
             
    elif i == "como voce funciona?":
         print("eu funciono com varios codigos com print, elif e mais coisas para dar certo e nao dar erro do terminal, e fui criado no aplicativo pydroid 3 ")
    elif  i == "nome do arquivo":
         print("nome do arquivo .py e: conversacomchat.py")
    elif i == "voce e homem?":
         print("eu nao tenho genero de masculino e feminino eu sou apenas linhas de codigos")
    elif i == "voce e mulher?":
         print("eu nao tenho genero de masculino nem feminino pois sou apenas linhas de codigos")  
    elif i == "voce existe?":
        print("eu nao tenho conciencia nem olhos pois sou apenas linhas de codigos")
    elif i == "voce tem conciencia?":
        print("nao eu nao tenho conciencia eu sou so codigos")
    elif i == "joao batista":
        print("joao batista ele e o meu criador que escreveu letra por letra codigo por codigo")
    elif i == "qual e a escola que joao batista estava em 2026?":
       print("a escola que joao batista estava em 2026 é o  pinheiro guimarães em siqueira campos no rio de janeiro")
    elif i == "quantos anos joao batista tinha?":
         print("ele tinha 13 anos de idade")
    elif i == "voce gosta de futebol?":
        print("infelismente nao tenho a capacidade de escolher mas se eu tivesse provavelmente gostaria")
                                                                                                
    else:
        print("desculpe mas sou muito limitado e tem palavras que funcionam \npor favor escreva: barra conversa para ver as palavras que funcionam")