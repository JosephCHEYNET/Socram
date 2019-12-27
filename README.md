# Socram CSV 2 OFX
La banque Socram ne permet de télécharger ses opérations qu'en fichier CSV ou XLS.
Ce projet fournit une application simple pour convertir les fichiers csv téléchargés en fichiers ofx.

* L'interface graphique est réalisée avec tkinter
* Par défaut le fichier source est le fichier le plus récent présent dans le répertoire téléchargement de l'utilisateur mais l'interface graphique permet de naviger pour en choisir un autre.
* Il est possible de saisir le solde pour l'ajouter au fichier OFX.

### Toutes les contributions sont les bienvenues.

Bugs connus:
* encodage des fichiers sous Mac OS
* manque la génération des ID uniques pour les transactions et les fichiers