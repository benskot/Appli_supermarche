T=[]
class Classe():
    def __init__(self,Nom,Annee,statut):
        self.Nom=str(input("Entrer le nom de la classe"))
        self.Annee=str(input("Entrer l'annee academique"))
        self.statut=bool(statut)


    def afficher(self):
        print("Le nom de la salle est",self.Nom,"et l'annee academique est",self.Annee)
        if self.statut==1:
          print("classe occupee")
        else:
          print("vide")

class Etudiant():
    def __int__(self):
        ""
    def affiche(self):
        n = int(input("Entrer le nombre d'etudiants"))
        for i in range(1,n+1):
            print("Entrer le nom de l'etudiant",i)
            n = str(input())
            T.append(n)
            print("Entrer l'age de l'etudiant",i)
            n = str(input())
            T.append(n)
            print("Entrer le sexe",i)
            n = str(input())
            T.append(n)
            print("entrer le matricule",i)
            n = str(input())
            T.append(n)
            print("entrer le contact",i)
            n = str(input())
            T.append(n)
            print("entrer la filiere",i)
            n = str(input())
            T.append(n)
            T.append("|||")
        print(T)
class cours():
    def __int__(self):
        ""
    def afficher(self):
        k = int(input("Entrer le nombre de matiere"))
        for i in range(1,k+1):
            print("Entrer le nom de la matiere",i)
            k = str(input())
            T.append(k)
            print("Entrer le nombre heure",i)
            k= str(input())
            T.append(k)
            print("Entrer le nom de l'enseignant",i)
            k= str(input())
            T.append(k)
            print("entrer le coef",i)
            k= str(input())
            T.append(k)
        print(T)


a2=Etudiant()
a2.affiche()
class Filiere(Etudiant):
    def __init__(self,nom_filiere,nbre_cours):
        Etudiant().__init__(self)
        self.nom_filiere=input("Entrer le nom de la filiere")
        self.nbre_cours=int(input("Entrer le nombre cours"))

