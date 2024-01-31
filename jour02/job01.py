import mysql.connector

# Paramètres de connexion à la base de données
host = "localhost"
user = "root"
password = "Nbvcxw.753"
database = "LaPlateforme"

# Connexion à la base de données
connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Création d'un curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()

# Exécution de la requête pour récupérer tous les étudiants
requete = "SELECT * FROM etudiant"
curseur.execute(requete)

# Récupération des résultats de la requête
resultats = curseur.fetchall()

# Affichage des résultats en console
for resultat in resultats:
    print(resultat)

# Fermeture du curseur et de la connexion
curseur.close()
connexion.close()
