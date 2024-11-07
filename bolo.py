class Bolo:
    def pessoa(self):
        pass

    def bolo(self):
        pass

class SimplesBolo(Bolo):
    def pessoa(self):
        return 2
    
    def bolo(self):
        return "Bolo de "
    
class DecoradorBolo(Bolo):
    def __init__(self, bolo: Bolo):
        self._bolo = bolo
    
    def pessoa(self):
        self._bolo.pessoa()

    def bolo(self):
        self._bolo.bolo()


class BoloDeNataEMorango(DecoradorBolo):
    def pessoa(self):
        return self._bolo.pessoa() + 3
    
    def bolo(self):
        return self._bolo.bolo() + ", nata e morango"
    
class BoloDeChocolate(DecoradorBolo):
    def pessoa(self):
        return self._bolo.pessoa() + 5
    
    def bolo(self):
        return self._bolo.bolo() + " e chocolate"
    
class BoloDeCenoura(DecoradorBolo):
    def pessoa(self):
        return self._bolo.pessoa() + 4
    
    def bolo(self):
        return self._bolo.bolo() + "Cenoura"
    

bolo_simples = SimplesBolo()
print(bolo_simples.bolo() )

bolo_cenoura = BoloDeCenoura(bolo_simples)
print(f"{bolo_cenoura.bolo()} para {bolo_cenoura.pessoa()} pessoas")

bolo_chocolate = BoloDeChocolate(bolo_cenoura)
print(f"{bolo_chocolate.bolo()} para {bolo_chocolate.pessoa()} pessoas")

bolo_nata = BoloDeNataEMorango(bolo_chocolate)
print(f"{bolo_nata.bolo()} para {bolo_nata.pessoa()} pessoas")