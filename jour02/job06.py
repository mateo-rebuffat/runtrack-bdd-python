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

# Exécution de la requête pour calculer la capacité totale des salles
requete = "SELECT SUM(capacite) AS capacite_totale FROM salle"
curseur.execute(requete)

# Récupération du résultat de la requête
resultat = curseur.fetchone()

# Affichage du résultat en console
capacite_totale = resultat[0]
print(f"La capacité de toutes les salles est de {capacite_totale}")

# Fermeture du curseur et de la connexion
curseur.close()
connexion.close()
