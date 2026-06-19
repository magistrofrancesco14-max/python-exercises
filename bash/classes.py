 # #  Una classe serve a raggruppare dati + azioni
# Senza classi:
# nome = Luca
# eta = 25
# print(nome)
# e sei avessi 100 persone?
# con le classi crei un modello

class Persona: # sempre con lettera maiuscola
    # costruttore (proprietà)
    def __init__(self, nome, cognome): # si mette self perchè è il riferimento all'istanza
        self.nome = nome
        self.cognone = cognome

    # metodo (azioni)
    def saluta(self):
        print("Ciao sono " + self.nome)
        

persona1 = Persona("Luca", "Rossi") # persona1 è l'istanza 
persona2 = Persona("Mario", "Verdi") # persona2 è l'istanza 

persona2.saluta() # per stampare

# # Ereditarietà
# una classe figlia eredita attributi e metodi della classe madre, ma può modificarli o estenderli
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome) # per ereditare i valori del costruttore, volendo si possono aggiungerne altri
        self.materia = materia

    def saluta(self):
        print("Ciao sono " + self.nome + " " + self.cognone) # sovrascrivere metodo (overriding)


insegnante1 = Insegnante("Anna", "Neri", "Matematica")

insegnante1.saluta()

print(insegnante1.materia) # per stampare la materia
