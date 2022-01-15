import os

sortie = os.popen("ipconfig") #exécuter la commande dos
print (sortie.read())
