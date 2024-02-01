-- Ajout des données à la table "étage"
INSERT INTO etage (nom, numéro, superficie) VALUES
('RDC', 0, 500)
('R+1', 1, 500)
-- Ajout des données à la table "salle"
INSERT INTO salle (nom, id_etage, capacite) VALUES
    ('Lounge', 1, 100),
    ('Studio Son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5);
