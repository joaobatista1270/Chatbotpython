print("ao escrever > barra conversa < vai mostras as palavras que funciona")
import time
import sys
while True:
    print(" ")
    i = input("digite: ").lower().strip()
    if i == "oi":
        print("oi tudo bem?")
        print(" ")
    elif i == "voce conhece o planeta terra?":
        print(" ")
        print("eu nao conheço pois sou linhas de codigos de linguagem python ")
        print(" ")
    elif i == "como esta?":
        print("oi infelismente nem sei se estou bem")
        print(" ")
    elif i == "como voce esta?":
         print(" ")
         print("infelismente nao tenho sentimentos pois sou apenas linha de codigos")
         print(" ")
    elif i == "encerrar":
         print(" ")
         print("encerrando...")
         time.sleep(1)
         sys.exit()
    elif i == "quem e voce?":
         print(" ")
         print("eu sou apenas uma linha de codigos")
         print(" ")
    elif i == "qual e o seu sonho?":
         print(" ")
         print("infelismente nao tenho celebro para ter sonhos eu eu queria ter sonhos") 
         print(" ")        
    elif i == "voce sabe matematica?":
         print(" ")
         print("eu nao fui feito para fazer matematicas eu fui feito para interagir")
         print(" ")
    elif  i == "barra conversa":
             print(" ")
             print(" > lista <")
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
             print("||| descriçao |||")
             print("                                          ")
             print("> modo abaixo  <")
             print("                                          ")
             print("||| modo matematica")
             print(" ")
             print(" ")
             print(" ")
    elif i == "voce tem sentimentos?":
             print(" ")
             print("nao eu nao sinto sentimentos pois so apenas linhas de codigos")
    elif i == "hoje vai chover?":
         print(" ")
         print("desculpe mas nao sei pois sou apenas linhas de codigos...")
         print(" ")
    elif i == "qual e o seu proposito?":
         print(" ")
         print("o meu proposito e apenas interagir")
         print(" ")
    elif i == "modo matematica":
         print(" ")
         print("escolha e digite: \n mais , menos , vezes , divisao")
         sn = input("digite um deles: ")
         print("                                       ")
         print("digite somente numeros ")
         e = float(input("primeiro numero: "))
         print(" ")
         h = float(input("segundo numero: "))

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
         print(" ")
         print("eu funciono com varios codigos com print, elif e mais coisas para dar certo e nao dar erro do terminal, e fui criado no aplicativo pydroid 3 ")
         print(" ")
    elif  i == "nome do arquivo":
         print(" ")
         print("nome do arquivo .py e: conversacomchat.py")
         print(" ")
    elif i == "voce e homem?":
         print(" ")
         print("eu nao tenho genero de masculino e feminino eu sou apenas linhas de codigos")
         print(" ")
    elif i == "voce e mulher?":
         print(" ")
         print("eu nao tenho genero de masculino nem feminino pois sou apenas linhas de codigos") 
         print(" ") 
    elif i == "voce existe?":
        print(" ")
        print("eu nao tenho conciencia nem olhos pois sou apenas linhas de codigos")
        print(" ")
    elif i == "voce tem conciencia?":
        print(" ")
        print("nao eu nao tenho conciencia eu sou so codigos")
        print(" ")
    elif i == "joao batista":
        print(" ")
        print("joao batista ele e o meu criador que escreveu letra por letra codigo por codigo")
        print(" ")
    elif i == "qual e a escola que joao batista estava em 2026?":
       print(" ")
       print("a escola que joao batista estava em 2026 é o  pinheiro guimarães em siqueira campos no rio de janeiro")
       print(" ")
    elif i == "quantos anos joao batista tinha?":
         print("ele tinha 13 anos de idade")
         print(" ")
    elif i == "voce gosta de futebol?":
        print(" ")
        print("infelismente nao tenho a capacidade de escolher mas se eu tivesse provavelmente gostaria")
        print(" ")
    elif i == "descriçao":
        print(" ") 
        print(f"olá sou joao batista e muito obrigado por testar o que eu criei \n eu gostaria de ser um jovem aprendiz em codigo pythom \n mais ainda não sou e ainda tenho 13 anos e so pode ser \n jovem aprendiz pelo menos aos 14 anos. \n mais enfim obrigado por testar!")                                                                                       
    else:
        print(" ")
        print("desculpe mas sou muito limitado e tem palavras que funcionam \npor favor escreva: > barra conversa < para ver as palavras que funcionam")
