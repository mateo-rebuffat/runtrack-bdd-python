import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def recuperer_employes_avec_service(self):
        requete = """
            SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS nom_service
            FROM employe
            LEFT JOIN service ON employe.id_service = service.id
        """
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        return resultats

    def inserer_employe(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Exemple d'utilisation de la classe Employe
employe_manager = Employe(host="localhost", user="root", password="Nbvcxw.753", database="LaPlateforme")

# Récupération de tous les employés avec leur service
employes = employe_manager.recuperer_employes_avec_service()
for employe in employes:
    print(employe)

# Fermeture de la connexion
employe_manager.fermer_connexion()
