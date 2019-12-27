#from tkinter import *
from tkinter import filedialog
from os import path

import itertools as it

from meza.io import read_csv, IterStringIO
from csv2ofx import utils
from csv2ofx.ofx import OFX
from csv2ofx.mappings.default import mapping

from operator import itemgetter

mapping = {
    'is_split': False,
    'has_header': True,
    'currency': 'EUR',
    'bank': 'Socram Banque',
    'account': 'toto',
    'date': itemgetter('Date'),
    'payee': itemgetter('Description'),
    'desc': itemgetter('Original Description'),
    'amount': itemgetter('Amount'),
    'type': itemgetter('Transaction Type'),
    'split_account': itemgetter('Category'),
}

"""mapping = {
    'delimiter' : ';',
    'account': 'compte joint',
    "date" : itemgetter("Date"),
    "desc" : itemgetter("Lib"),
    "amount" : itemgetter("Debit")
}"""
"""     "Debit" : itemgetter("Débit (EUR)"),
    "Credit" : itemgetter("Crédit (EUR)")
    #"DateAvailable" : itemgetter("Date de valeur"),
    """

filename = filedialog.askopenfilename(
    initialdir=(path.expanduser("~/Downloads")),
    title="Choisisez le fichier à convertir",
    filetypes=(("csv files", "*.csv"),("all files", "*.*"))
)

def convertir(filename):
    ofx = OFX(mapping)
    records = read_csv(filename,  delimiter=';')
    groups = ofx.gen_groups(records)
    trxns = ofx.gen_trxns(groups)
    cleaned_trxns = ofx.clean_trxns(trxns)
    data = utils.gen_data(cleaned_trxns)
    header = ofx.header()
    body = ofx.gen_body(data)
    footer = ofx.footer()
    content = it.chain(header,body, footer)

    for line in IterStringIO(content):
        print(line)
    #print("convertion :"+str(solde.get()))

convertir(filename)


""" # On crée une fenêtre, racine de notre interface
fenetre = Tk()
# fenetre.withdraw()
# fenetre.resizable(False, True)
# convertion = Tk() labelSolde = Label(fenetre, text="Saisisez le solde")
labelSolde.pack(fill=X)

saisieSolde = Entry(fenetre, textvariable=solde, width=30)
saisieSolde.pack(fill=X)

bouton_conversion = Button(fenetre, text="Convertir", command=convertir)
bouton_conversion.pack(side="left")

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right")

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()"""



""" champ_nomfichier = Label(fenetre, text=filename)
champ_nomfichier.pack()

solde = DoubleVar() """


""" labelSolde = Label(fenetre, text="Saisisez le solde")
labelSolde.pack(fill=X)

saisieSolde = Entry(fenetre, textvariable=solde, width=30)
saisieSolde.pack(fill=X)

bouton_conversion = Button(fenetre, text="Convertir", command=convertir)
bouton_conversion.pack(side="left")

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right")

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop() """

# cadre = LabelFrame(fenetre
#     fenetre,
#     text="Données d'entrée",
#     width=768,
#     height=576,
#     borderwidth=2,
#     fg="white",
#     bg="blue",
# )
# cadre.pack()

# laberChoixFichier = Label(cadre, text="Choisisez votre fichier")
# laberChoixFichier.pack(fill=X)

# cheminFichier = StringVar()
# saisieCheminFichier = Entry(cadre, textvariable=cheminFichier, width=30)
# saisieCheminFichier.pack(fill=X)

# choixFichier = filedialog(cadre, title="filedialog")
# choixFichier.pack(fill=X)


