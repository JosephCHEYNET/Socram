import os
from os import path
_, ext = os.path.splitext('/foo/bar/baz.txt')
print(ext) # => .txt


import glob
monRepertoire = path.expanduser("~/Downloads")+'/*.csv'
MaxDate = 0
fichierRetenu = ''
fichiers = glob.glob(monRepertoire)
for fichier in fichiers:
	if os.path.getctime(fichier) > MaxDate:
		fichierRetenu = fichier
		MaxDate = os.path.getctime(fichier)
print(fichierRetenu)