import csv
#def afficher_ligne(): #afficher toute les lignes
 #   with open('data/data.csv', mode="r", encoding="UTF-8",) as fichier:
  #      fichier_csv=csv.DictReader(fichier)
   #     for ligne in fichier_csv:#affiche toutes les colonnes
    #        print(ligne)

#def afficher_date():  #afficher toute les lignes
#    with open('data/data.csv', mode="r", encoding="UTF-8" ) as fichier:
#        fichier_csv=csv.DictReader(fichier)
#        for date in fichier_csv:#affiche
#            return(date["date"])

#def afficher_mesure(): afficher toute les lignes
  #  with open('data/data.csv', mode="r",encoding="UTF-8") as fichier:
   #     fichier_csv=csv.DictReader(fichier)
    #    for mesure in fichier_csv:
     #       print(mesure["mesure"])

#def afficher_limitation(): afficher tout les lignes
 #   with open('data/data.csv', mode="r", encoding="UTF-8") as fichier:
  #      fichier_csv=csv.DictReader(fichier, delimiter=',')
   #     for limite in fichier_csv:
    #        print(limite["limite"])


#def afficher_flash():#affiche l'ecart de la limitation de vitesse
  #  with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
   #     fichier_csv=csv.DictReader(fichier)
    #    for vitesse in fichier_csv:
     #       depasser=int(vitesse["mesure"]) - int(vitesse["limite"])
      #      if depasser>0:
       #         print("relever à une vitesse de",depasser, "pour une limitation de",vitesse["limite"],"km/h à la date du ", vitesse["date"])


#Mon erreur
#def afficher_flash(limite):
 #   with open ('data/data.csv', mode='r' , encoding="UTF-8") as fichier:
  #      fichier_csv=csv.DictReader(fichier, delimiter=',')
   #     for depasser in fichier_csv:
    #        vitesse=int(depasser["mesure"])-limite
     #       if vitesse>limite:
      #          print("voici la vitesse", vitesse,"de", depasser["date"])

#afficher_flash(70)
#Mon erreur
#vitesse=int(depasser["mesure"])-limite
#if vitesse>limite:

#correction apportée par l'IA 

#for ligne in fichier_csv:
 #           try:
  #              mesure=int(ligne["mesure"])
   #             limite=int(ligne["limite"])
    #        except ValueError:
     #           continue
      #      if limite==limitation and mesure>limite:


def afficher_70(limitation):#affiche les vitesses supérieures à 70 
    # affiche les passages sur une route limitée à limite_voulue où la mesure dépasse cette limite
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
        fichier_csv = csv.DictReader(fichier, delimiter=',')
        for ligne in fichier_csv:
            try:
                mesure=int(ligne["mesure"])
                limite=int(ligne["limite"])
            except ValueError:
                continue
            if limite==limitation and mesure>limite:
                print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")

def afficher_80(limitation): #affiche les vitesses supérieures à 70km/h
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
            fichier_csv = csv.DictReader(fichier, delimiter=',')
            for ligne in fichier_csv:
                try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
                except ValueError:
                    continue
                if limite==limitation and mesure>limite:
                    print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")

def afficher_90(limitation): #affiche les vitesses supérieures à 90km/h
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
            fichier_csv = csv.DictReader(fichier, delimiter=',')
            for ligne in fichier_csv:
                try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
                except ValueError:
                    continue
                if limite==limitation and mesure>limite:
                    print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")


def afficher_90(limitation): #affiche les vitesses supérieures à 90km/h
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
            fichier_csv = csv.DictReader(fichier, delimiter=',')
            for ligne in fichier_csv:
                try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
                except ValueError:
                    continue
                if limite==limitation and mesure>limite:
                    print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")

def afficher_110(limitation): #affiche les vitesses supérieures à 110km/h
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
            fichier_csv = csv.DictReader(fichier, delimiter=',')
            for ligne in fichier_csv:
                try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
                except ValueError:
                    continue
                if limite==limitation and mesure>limite:
                    print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")

def afficher_130(limitation):#affiche les vitesses supérieures à 130km/h
    with open('data/data.csv', mode='r', encoding="UTF-8") as fichier:
            fichier_csv = csv.DictReader(fichier, delimiter=',')
            for ligne in fichier_csv:
                try:
                    mesure=int(ligne["mesure"])
                    limite=int(ligne["limite"])
                except ValueError:
                    continue
                if limite==limitation and mesure>limite:
                    print("Relevé à une vitesse de",ligne["mesure"],"km/h" "sur une route limitée à", limite,"km/h")                    


        
            







            




    

       










#afficher_ligne()
#afficher_date()
#afficher_mesure()
#afficher_flash()
#afficher_limitation()
afficher_70(70)
afficher_80(80)
afficher_90(90)
afficher_110(110)
afficher_130(130)



        

