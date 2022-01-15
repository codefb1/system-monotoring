import os

sortie = os.popen("ipconfig") #exécuter la commande
print (sortie.read())
