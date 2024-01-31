import mysql.connector
from datetime import datetime

class ZooManager:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def ajouter_cage(self, superficie, capacite_max):
        requete = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        valeurs = (superficie, capacite_max)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def ajouter_animal(self, nom, race, id_type_cage, date_naissance, pays_origine):
        requete = """
            INSERT INTO animal (nom, race, id_type_cage, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """
        valeurs = (nom, race, id_type_cage, date_naissance, pays_origine)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_animal(self, id_animal):
        requete = "DELETE FROM animal WHERE id = %s"
        valeurs = (id_animal,)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def modifier_animal(self, id_animal, nom, race, id_type_cage, date_naissance, pays_origine):
        requete = """
            UPDATE animal
            SET nom=%s, race=%s, id_type_cage=%s, date_naissance=%s, pays_origine=%s
            WHERE id=%s
        """
        valeurs = (nom, race, id_type_cage, date_naissance, pays_origine, id_animal)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def afficher_animaux(self):
        requete = "SELECT * FROM animal"
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        print("Animaux dans le zoo :")
        for animal in resultats:
            print(animal)

    def afficher_animaux_cages(self):
        requete = """
            SELECT cage.id AS id_cage, cage.superficie, cage.capacite_max, animal.*
            FROM cage
            LEFT JOIN animal ON cage.id = animal.id_type_cage
        """
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        print("Animaux dans les cages :")
        for animal_cage in resultats:
            print(animal_cage)

    def calculer_superficie_totale(self):
        requete = "SELECT SUM(superficie) FROM cage"
        self.curseur.execute(requete)
        superficie_totale = self.curseur.fetchone()[0]
        print(f"La superficie totale des cages est de {superficie_totale} m2")

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

if __name__ == "__main__":
    zoo_manager = ZooManager(host="localhost", user="root", password="Nbvcxw.753", database="zoo")

    while True:
        print("\nMenu :")
        print("1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Supprimer un animal")
        print("4. Modifier un animal")
        print("5. Afficher tous les animaux")
        print("6. Afficher les animaux dans les cages")
        print("7. Calculer la superficie totale des cages")
        print("0. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "0":
            break
        elif choix == "1":
            superficie = input("Superficie de la cage : ")
            capacite_max = input("Capacité maximale de la cage : ")
            zoo_manager.ajouter_cage(superficie, capacite_max)
        elif choix == "2":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            id_type_cage = input("ID du type de cage : ")
            date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
            pays_origine = input("Pays d'origine : ")
            zoo_manager.ajouter_animal(nom, race, id_type_cage, date_naissance, pays_origine)
        elif choix == "3":
            id_animal = input("ID de l'animal à supprimer : ")
            zoo_manager.supprimer_animal(id_animal)
        elif choix == "4":
            id_animal = input("ID de l'animal à modifier : ")
            nom = input("Nouveau nom de l'animal : ")
            race = input("Nouvelle race de l'animal : ")
            id_type_cage = input("Nouvel ID du type de cage : ")
            date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD) : ")
            pays_origine = input("Nouveau pays d'origine : ")
            zoo_manager.modifier_animal(id_animal, nom, race, id_type_cage, date_naissance, pays_origine)
        elif choix == "5":
            zoo_manager.afficher_animaux()
        elif choix == "6":
            zoo_manager.afficher_animaux_cages()
        elif choix == "7":
            zoo_manager.calculer_superficie_totale()
