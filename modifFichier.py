from tkinter import filedialog
from os import path
import datetime

def conversionDate(date):
    dateConvertie = date.split('/')
    return dateConvertie[2]+dateConvertie[1]+dateConvertie[0]


"""filename = filedialog.askopenfilename(
    initialdir=(path.expanduser("~/Downloads")),
    title="Choisisez le fichier à convertir",
    filetypes=(("csv files", "*.csv"), ("all files", "*.*")),
)"""
chemin = './SOCRAM'
monChemin = path.dirname(chemin)
nomFichier = path.basename(chemin)
#génération des lignes
lignes = ''
minDate = 0
maxDate = 0

with open(chemin+'.csv', 'r',8192,'iso-8859-1') as fichierCsv:   
    content = fichierCsv.readlines()
    content.pop(0)
    for ligne in content:
        ligne = ligne.replace("&#039;","'")
        splitLine = ligne.split(';')
        lignes += 'dateOperation'+conversionDate(splitLine[0])+'\n'
        lignes += 'libelle'+splitLine[1]+'\n'
        lignes += 'dateValeur'+conversionDate(splitLine[2])+'\n'
        lignes += 'debit'+splitLine[3]+'\n'
        lignes += 'credit'+splitLine[4]+'\n'
#génération du fichier ofx
with open(chemin+'.ofx', 'w') as fichierOfx:
    #ecriture de l entete
    fichierOfx.write('OFXHEADER:100'+'\n')
    fichierOfx.write('DATA:OFXSGML'+'\n')
    fichierOfx.write('VERSION:102'+'\n')
    fichierOfx.write('SECURITY:NONE'+'\n')
    fichierOfx.write('ENCODING:USASCII'+'\n')
    fichierOfx.write('CHARSET:1252'+'\n')
    fichierOfx.write('COMPRESSION:NONE'+'\n')
    fichierOfx.write('OLDFILEUID:NONE'+'\n')
    fichierOfx.write('NEWFILEUID:NONE'+'\n')
    #ouverture du xml
    fichierOfx.write('<OFX>'+'\n')
    fichierOfx.write('<SIGNONMSGSRSV1>'+'\n')
    fichierOfx.write('<SONRS>'+'\n')
    fichierOfx.write('<STATUS>'+'\n')
    fichierOfx.write('<CODE>0'+'\n')
    fichierOfx.write('<SEVERITY>INFO'+'\n')
    fichierOfx.write('</STATUS>'+'\n')
    # date du jour à inscrire
    fichierOfx.write('<DTSERVER>20191117'+'\n')
    fichierOfx.write('<LANGUAGE>FR'+'\n')
    fichierOfx.write('</SONRS>'+'\n')
    fichierOfx.write('</SIGNONMSGSRSV1>'+'\n')
    fichierOfx.write('<BANKMSGSRSV1>'+'\n')
    fichierOfx.write('<STMTTRNRS>'+'\n')
    # TRNUID à inscrire
    fichierOfx.write('<TRNUID>99fe3986-a467-4080-915b-a4e084b5ff49'+'\n')
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
    # date à inscrire
    fichierOfx.write('<DTSTART>20191028'+'\n')
    # date à inscrire
    fichierOfx.write('<DTEND>20191115'+'\n')


print('fin')



