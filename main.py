import csv
import os #idée de l'IA (permet d'intéragir avec le système d'exploitation)

def afficher_exces(limitation):
    with open("data/data.csv", mode="r", encoding="utf-8") as fichier:
        fichier_csv = csv.DictReader(fichier, delimiter=",")
        for ligne in fichier_csv:
            try:
                limite = int(ligne["limite"])
                mesure = int(ligne["mesure"])
            except ValueError:
                continue
            if limite == limitation and mesure > limite:
                ecart = mesure - limite
                print(
                    f"Relevé à {mesure} km/h sur une route limitée à {limite} km/h (+{ecart} km/h)"
                )


def creer_page_html(limitation, morceau, numero_page, nb_pages, total_lignes):  # code généré par IA pour créer une page html
    nom_fichier = f"pages/limitation_{limitation}_page{numero_page}.html"

    with open(nom_fichier, mode="w", encoding="utf-8") as page_html:
        page_html.write("<!DOCTYPE html>\n")
        page_html.write('<html lang="fr">\n')
        page_html.write("<head>\n")
        page_html.write('    <meta charset="utf-8">\n')
        page_html.write(
            f"    <title>Excès {limitation} km/h - Page {numero_page}/{nb_pages}</title>\n"
        )
        page_html.write("</head>\n")
        page_html.write("<body>\n")
        page_html.write(f"    <h1>Limitation à {limitation} km/h</h1>\n")
        page_html.write(
            f"    <p>Page {numero_page} sur {nb_pages} (Total : {total_lignes} excès relevés)</p>\n"
        )
        page_html.write('    <table border="1" width="100%">\n')
        page_html.write("        <tr>\n")
        page_html.write("            <th>Limitation</th>\n")
        page_html.write("            <th>Vitesse mesurée</th>\n")
        page_html.write("            <th>Excès</th>\n")
        page_html.write("        </tr>\n")

        for limite, mesure, ecart in morceau:
            page_html.write("        <tr>\n")
            page_html.write(f"            <td>{limite} km/h</td>\n")
            page_html.write(f"            <td>{mesure} km/h</td>\n")
            page_html.write(f"            <td>+{ecart} km/h</td>\n")
            page_html.write("        </tr>\n")

        page_html.write("    </table>\n")
        page_html.write("    <p>\n")

        if numero_page > 1:
            page_html.write(
                f'        <a href="limitation_{limitation}_page{numero_page - 1}.html">Page précédente</a> '
            )

        if numero_page < nb_pages:
            page_html.write(
                f'        <a href="limitation_{limitation}_page{numero_page + 1}.html">Page suivante</a>'
            )

        page_html.write("\n    </p>\n")
        page_html.write("</body>\n")
        page_html.write("</html>\n")


def generer_pages_limitation(limitation, lignes_trouvees, par_page=500): #code généré par IA pour générer les pages suivantes
    os.makedirs("pages", exist_ok=True)
    total_lignes = len(lignes_trouvees)

    if total_lignes == 0:
        print(f"Limitation {limitation} km/h : aucun excès trouvé.")
        return

    nb_pages = (total_lignes + par_page - 1) // par_page

    for numero_page in range(1, nb_pages + 1):
        debut = (numero_page - 1) * par_page
        fin = debut + par_page
        morceau = lignes_trouvees[debut:fin]
        creer_page_html(limitation, morceau, numero_page, nb_pages, total_lignes)

    print(
        f"Limitation {limitation} km/h : {total_lignes} excès -> {nb_pages} page(s) générée(s)."
    )


def generer_tout(par_page=500):
    limitations = [70, 80, 90, 110, 130]
    donnees_par_limite = {vitesse: [] for vitesse in limitations}

    print("Lecture de data/data.csv en cours (~9,6M de lignes)...")

    with open("data/data.csv", mode="r", encoding="utf-8") as fichier:
        fichier_csv = csv.DictReader(fichier, delimiter=",")
        for index, ligne in enumerate(fichier_csv, start=1):
            if index % 500000 == 0:
                print(f"{index} lignes lues...")

            try:
                limite = int(ligne["limite"])
                mesure = int(ligne["mesure"])
            except KeyError:
                print("Colonnes disponibles :", fichier_csv.fieldnames)
                return
            except ValueError:
                continue

            if limite in donnees_par_limite and mesure > limite:
                donnees_par_limite[limite].append((limite, mesure, mesure - limite))

    print("Lecture terminée, génération des pages HTML...")
    for vitesse in limitations:
        generer_pages_limitation(vitesse, donnees_par_limite[vitesse], par_page=par_page)


generer_tout(par_page=500)
                         


     




             







    








### Mon idée + celle d' l'IA crée une fonctione qui permet de récupérer les voitures qui
#qui ont fait un excès de vitesse au delà de la limite de vitesse recommandé 70km/h
#def limitation_70(limitation):
#    with open("data/data.csv", mode="r", encoding="utf-8") as fichier:
 #       fichier_csv=csv.DictReader(fichier, delimiter=',')

  #  with open("pages/limitation_70.html", mode="w", encoding="utf-8") as fichier_html:
   #     fichier_html.write('''<!DOCTYPE html>
#<html lang="fr">
#<head>
 #   <meta charset="utf-8">
  #  <meta name="viewport" content="width=device-width, initial-scale=1.0">
   # <link rel="stylesheet" href="../radar.css">
    #<title>Limitation 70</title>
#</head>
#<body>
 #   <h1>Limitation à 70km/h</h1>
  #  <table border="1" width="100%">
   #     <tr>
    #        <th>Limitation</th>
     #       <th>Excès</th>
      #  </tr>
#''')

    #    for vitesse in fichier_csv:
     #       try:
      #          limite=int(vitesse["limite"])
       #         exces=int(vitesse["mesure"])
        #    except ValueError:
         #       continue
          #  if limite==limitation and exces>limite:
           #     fichier_html.write(f'''</tr>
        #<td>{limite}</td>
        #<td>{exces}</td>
    #</tr>
#''')
 #           fichier_html('''   </table>
#</body>
#</html>
#''')
            
#limitation_70(70)

        


