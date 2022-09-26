#Louis Emery 401
#26 septembre 2022

#demande la phrase a l'utilisateur
phrase = input(str("votre phrase: "))

#definir la fonction
def count_word(phrase):
    #strip la phrase pour enlever les espaces inutiles
    phrase2 = phrase.strip(" ")
    #split la phrae pour connaitre le nombre de mots
    phrase3 = phrase2.split(" ")
    #amene le nombre de mots pour lutiliser en dehors de la phrase
    return(len(phrase3))
#definir la variable ndm en etant le nombre de mots definit dans la fonction
ndm = count_word(phrase)

#print le nombre de mots
print(ndm)