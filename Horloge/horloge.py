import time
import threading

class Horloge:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        self.mode_12h = False
        self.pause = False
        self.alarme = None

    def afficher_heure(self):
        if self.mode_12h:
            am_pm = "AM"
            heures_affichage = self.heures
            if self.heures > 12:
                heures_affichage -= 12
                am_pm = "PM"
            print(f"{heures_affichage:02d}:{self.minutes:02d}:{self.secondes:02d} {am_pm}")
        else:
            print(f"{self.heures:02d}:{self.minutes:02d}:{self.secondes:02d}")

    def regler_heure(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def regler_alarme(self, heures, minutes, secondes):
        self.alarme = (heures, minutes, secondes)

    def verifier_alarme(self):
        if self.alarme and (self.heures, self.minutes, self.secondes) == self.alarme:
            print("Alarme !")

    def changer_mode_affichage(self):
        self.mode_12h = not self.mode_12h

    def mettre_en_pause(self):
        self.pause = True

    def relancer(self):
        self.pause = False

    def demarrer(self):
        while True:
            if not self.pause:
                self.secondes += 1
                if self.secondes == 60:
                    self.secondes = 0
                    self.minutes += 1
                    if self.minutes == 60:
                        self.minutes = 0
                        self.heures += 1
                        if self.heures == 24:
                            self.heures = 0

                self.afficher_heure()
                self.verifier_alarme()

            time.sleep(1)

def interaction_utilisateur(horloge):
    while True:
        print("\nOptions:")
        print("1. Changer l'heure")
        print("2. Changer l'alarme")
        print("3. Mettre en pause/relancer")
        print("4. Changer le format d'affichage (12/24 heures)")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5): ")

        if choix == '1':
            heures = int(input("Entrez les heures : "))
            minutes = int(input("Entrez les minutes : "))
            secondes = int(input("Entrez les secondes : "))
            horloge.regler_heure(heures, minutes, secondes)

        elif choix == '2':
            heures = int(input("Entrez les heures de l'alarme : "))
            minutes = int(input("Entrez les minutes de l'alarme : "))
            secondes = int(input("Entrez les secondes de l'alarme : "))
            horloge.regler_alarme(heures, minutes, secondes)

        elif choix == '3':
            if horloge.pause:
                horloge.relancer()
            else:
                horloge.mettre_en_pause()

        elif choix == '4':
            horloge.changer_mode_affichage()

        elif choix == '5':
            horloge.mettre_en_pause()
            break

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

# Exemple d'utilisation
horloge = Horloge(12, 0, 0)
thread = threading.Thread(target=horloge.demarrer)
thread.start()

interaction_utilisateur(horloge)
