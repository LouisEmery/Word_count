#Louis Emery 401
#26 septembre 2022

#demande la phrase a l'utilisateur
phrase = input(str("votre phrase: "))

#definir la fonction
def count_word(phrase):
    #strip la phrase pour enlever les espaces inutiles
    stripped_phrase = phrase.strip(" ")
    #split la phrae pour connaitre le nombre de mots
    nombre_de_mots = stripped_phrase.split(" ")
    #amene le nombre de mots pour lutiliser en dehors de la phrase
    nbr = (len(nombre_de_mots))
    return nbr
#definir la variable ndm en etant le nombre de mots definit dans la fonction
ndm = count_word(phrase)

#print le nombre de mots
print(ndm)
