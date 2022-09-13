#definir la fonction
def WordCount():
    #demande la phrase a l'utilisateur
    phrase = input("votre phrase: ")
    #strip la phrase pour enlever les espaces inutiles
    phrase2 = phrase.strip(" ")
    #split la phrae pour connaitre le nombre de mots
    phrase3 = phrase2.split(" ")
    #print le nombre de mots
    print(len(phrase3))
WordCount()