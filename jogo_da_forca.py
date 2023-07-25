def jogar():
    
    print("""***** Bem vindo ao jogo da Forca!*****
       ________
    //        |
    |         O
    |        /|\\
    |        / \\
    |
    \\_________""")

    palavra_secreta = "bufalo".upper()
    letras_acertadas=['_' for letra in palavra_secreta] # Adapta a quantidade de '_' para a palavra escolhida
    letras_faltando = str(letras_acertadas.count('_')) 

    enforcou = False
    acertou = False
    erros = 0

    print("Palavra:",*letras_acertadas)
    while(not acertou and not enforcou):
        
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        
        index = 0

        if(chute in palavra_secreta):

         for letra in palavra_secreta:

            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra{letra} na posição {index}")
                letras_acertadas[index] = letra
                letras_faltando = str(letras_acertadas.count('_'))

            index = index+1   

        else:
           erros +=1     

        enforcou = erros == 6

        if erros==1:
           
           print(""" 
           ________
         //        |
         |         O
         |        
         |        
         |
         \\_________""")
           
        elif erros == 2:
           
           print("""
           ________
         //        |
         |         O
         |         |
         |        
         |
         \\_________""")
        
        elif erros == 3:
           
           print(""" 
            ________
         //        |
         |         O
         |        /|
         |        
         |
         \\_________""")
           
        elif erros == 4:
           
           print("""  
            ________
         //        |
         |         O
         |        /|\\
         |         
         |
         \\_________""")   
           
        elif erros == 5:
           
           print("""   
            ________
         //        |
         |         O
         |        /|\\
         |        / 
         |
         \\_________""") 

           
           


        acertou = '_' not in letras_acertadas 
        print("Palavra: ",*letras_acertadas)
        print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
        print ("Jogando...")
        
    if acertou:
       print("****** Parabéns Voçe ganhou ******")
    elif enforcou:
       print("""
           ****** Você Perdeu!! ******
       ________
       //        |
       |         O
       |        /|\\
       |        / \\
       |
       \\_________
          """)    
    print("Fim do jogo")

if (__name__=="__main__"):   
    jogar()