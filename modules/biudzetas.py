import pickle
from modules.islaiduirasas import IslaiduIrasas
from modules.pajamuirasas import PajamuIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as r_file:
                zurnalas = pickle.load(r_file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_zurnala(self, zurnalas):
        with open("zurnalas.pkl", 'wb') as w_file:
            pickle.dump(zurnalas, w_file)

    def prideti_pajamas(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala(self.zurnalas)

    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        irasas = PajamuIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala(self.zurnalas)

    def perziureti_zurnala(self):
        for irasas in self.zurnalas:
            print(irasas)

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            elif type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas:", suma)