import csv
def compteur_limitation(limitation,chemin="data/data.csv"): 
    compteur=0
    with open(chemin,mode='r',encoding='utf-8') as fichier:
          fichier_csv = csv.DictReader(fichier, delimiter=';')
          for ligne in fichier_csv:
               try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
               except ValueError:
                    continue
               if limitation==limite and mesure>limitation:
                    compteur=compteur+1
    return compteur

print(compteur_limitation(70,"data/test.csv"))