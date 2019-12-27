from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from os import path
from os import listdir
from os.path import isfile, join
import datetime
import glob

def rechercheDuDernierFichierOfxCreeDansLeDossierTelechargement():
	monRepertoire = path.expanduser("~/Downloads")+'/*.csv'
	maxDate = 0
	fichierRetenu = ''
	fichiers = glob.glob(monRepertoire)
	for fichier in fichiers:
		if os.path.getctime(fichier) > maxDate:
			fichierRetenu = fichier
			maxDate = os.path.getctime(fichier)
	return fichierRetenu

#fonction qui sert à transformer les dates au bon format
def conversionDate(date):
    dateConvertie = date.split('/')
    return dateConvertie[2]+dateConvertie[1]+dateConvertie[0]

def choixFichier():
	filename.set(filedialog.askopenfilename(initialdir=(path.expanduser("~/Downloads")),title="Choisisez le fichier à convertir",filetypes=(("csv files", "*.csv"), ("csv files", "*.csv")),))

def generationDesLignes():
	lignes = ''
	minDate = 99999999
	maxDate = 0
	with open(filename.get(), 'r',8192,'iso-8859-1') as fichierCsv:   
		content = fichierCsv.readlines()
		content.pop(0)
		for ligne in content:
			ligne = ligne.replace("&#039;","'")
			splitLine = ligne.split(';')
			dateOperation = conversionDate(splitLine[0])
			minDate = min(minDate,int(dateOperation))
			maxDate = max(maxDate, int(dateOperation))
			lignes += '<STMTTRN>'+'\n'
			amount = 0
			if splitLine[3] != '':
				lignes += '<TRNTYPE>DEBIT'+'\n'
				amount = '-'+splitLine[3].replace(',','.')
				pass
			else:
				lignes += '<TRNTYPE>CREDIT'+'\n'
				amount = splitLine[4].replace(',','.')
				pass
			lignes += '<DTPOSTED>'+dateOperation+'\n'   
			lignes += '<DTAVAIL>'+conversionDate(splitLine[2])+'\n'
			debit = splitLine[3].replace(',','.')
			lignes += '<TRNAMT>'+amount+'\n'
			lignes += '<MEMO>'+splitLine[1]+'\n'
			#TODO génération du FITID
			#lignes += '<FITID>fa98edfb50b7b7e0dbda334a0c7abea72fa687e6'+'\n'
			lignes += '</STMTTRN>>'+'\n'
	return lignes, minDate, maxDate

def generationFichierOfx():
	lignes, minDate, maxDate = generationDesLignes()
	with open(filename.get().replace('.csv','.ofx').replace('.CSV','.OFX'), 'w') as fichierOfx:
		#*************** écrire de l'entete **************
		fichierOfx.write('OFXHEADER:100'+'\n')
		fichierOfx.write('DATA:OFXSGML'+'\n')
		fichierOfx.write('VERSION:102'+'\n')
		fichierOfx.write('SECURITY:NONE'+'\n')
		fichierOfx.write('ENCODING:USASCII'+'\n')
		fichierOfx.write('CHARSET:1252'+'\n')
		fichierOfx.write('COMPRESSION:NONE'+'\n')
		fichierOfx.write('OLDFILEUID:NONE'+'\n')
		fichierOfx.write('NEWFILEUID:NONE'+'\n')
		#debut du xml
		fichierOfx.write('<OFX>'+'\n')
		fichierOfx.write('<SIGNONMSGSRSV1>'+'\n')
		fichierOfx.write('<SONRS>'+'\n')
		fichierOfx.write('<STATUS>'+'\n')
		fichierOfx.write('<CODE>0'+'\n')
		fichierOfx.write('<SEVERITY>INFO'+'\n')
		fichierOfx.write('</STATUS>'+'\n')
		dateDuJour = datetime.datetime.now().strftime('%Y%m%d')
		fichierOfx.write('<DTSERVER>'+str(datetime.datetime.now().strftime('%Y%m%d'))+'\n')
		fichierOfx.write('<LANGUAGE>FR'+'\n')
		fichierOfx.write('</SONRS>'+'\n')
		fichierOfx.write('</SIGNONMSGSRSV1>'+'\n')
		fichierOfx.write('<BANKMSGSRSV1>'+'\n')
		fichierOfx.write('<STMTTRNRS>'+'\n')
		# TRNUID à inscrire
		#fichierOfx.write('<TRNUID>99fe3986-a467-4080-915b-a4e084b5ff49'+'\n')
		fichierOfx.write('<STATUS>'+'\n')
		fichierOfx.write('<CODE>0'+'\n')
		fichierOfx.write('<SEVERITY>INFO'+'\n')
		fichierOfx.write('</STATUS>'+'\n')
		fichierOfx.write('<STMTRS>'+'\n')
		fichierOfx.write('<CURDEF>EUR'+'\n')
		fichierOfx.write('<BANKACCTFROM>'+'\n')
		fichierOfx.write('<BANKID>Generic'+'\n')
		fichierOfx.write('<ACCTID>SOCRAM'+'\n')
		fichierOfx.write('<ACCTTYPE>CHECKING'+'\n')
		fichierOfx.write('</BANKACCTFROM>'+'\n')
		fichierOfx.write('<BANKTRANLIST>'+'\n')
		fichierOfx.write('<DTSTART>'+str(minDate)+'\n')
		fichierOfx.write('<DTEND>'+str(maxDate)+'\n')
		#************** écrire des lignes **************
		fichierOfx.write(lignes)
		#************** écrire de la fin du ofx **************
		fichierOfx.write('</BANKTRANLIST>'+'\n')
		fichierOfx.write('<LEDGERBAL>'+'\n')
		#écriture du solde
		fichierOfx.write('<BALAMT>'+str(solde.get())+'\n')
		fichierOfx.write('<DTASOF>'+str(maxDate)+'\n')
		fichierOfx.write('</LEDGERBAL>'+'\n')
		fichierOfx.write('</STMTRS>'+'\n')
		fichierOfx.write('</STMTTRNRS>'+'\n')
		fichierOfx.write('</BANKMSGSRSV1>'+'\n')
		fichierOfx.write('</OFX>'+'\n')

def convertir():
	try:
		test = solde.get()
	except:
		messagebox.showerror("erreur", "le solde doit être un nombre")
	generationFichierOfx()
	fenetre.destroy()
		
"""
	nomChemin = path.dirname(filename.get())
	nomFichier = path.basename(filename.get())"""

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.minsize(540,1)
fenetre.title('CSV 2 OFX')
fenetre.resizable(True, False)
#initialisation des variables
filename = StringVar()
filename.set(rechercheDuDernierFichierOfxCreeDansLeDossierTelechargement())
solde = DoubleVar()
# fenetre.withdraw()
cadreFichier = LabelFrame(fenetre, borderwidth=2, text='Fichier csv')
cadreFichier.pack(fill=X)
labelNomFichier = Label(cadreFichier, textvariable=filename)
labelNomFichier.pack(side="left")
bouton_choixFichier = Button(cadreFichier, text='choisir', command=choixFichier)
bouton_choixFichier.pack(side="right")
cadreSolde = LabelFrame(fenetre, borderwidth=2,text="Solde")
cadreSolde.pack(fill=X)
saisieSolde = Entry(cadreSolde, textvariable=solde, width=30)
saisieSolde.pack(fill=X)
cadreBoutons = Frame(fenetre, borderwidth=2)
cadreBoutons.pack(fill=X)
bouton_conversion = Button(cadreBoutons, text="Convertir", command=convertir, fg="green")
bouton_conversion.pack(fill=X)
bouton_quitter = Button(cadreBoutons, text="Quitter", command=fenetre.destroy, fg="red")
bouton_quitter.pack(fill=X)



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()





