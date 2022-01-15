import os

sortie = os.popen("ipconfig")
print (sortie.read())
