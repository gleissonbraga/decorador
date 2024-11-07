import unittest
from bolo import SimplesBolo, BoloDeCenoura, BoloDeChocolate, BoloDeNataEMorango

class TestBolo(unittest.TestCase):
    def setUp(self):
        self.bolo_simples = SimplesBolo()
        self.bolo_cenoura = BoloDeCenoura(self.bolo_simples)
        self.bolo_chocolate = BoloDeChocolate(self.bolo_cenoura)
        self.bolo_nata = BoloDeNataEMorango(self.bolo_chocolate)

    def test_bolo_simples(self):
        self.assertEqual(self.bolo_simples.bolo(), "Bolo de ")
        self.assertEqual(self.bolo_simples.pessoa(), 2)

    def test_bolo_cenoura(self):
        self.assertEqual(self.bolo_cenoura.bolo(), "Bolo de Cenoura")
        self.assertEqual(self.bolo_cenoura.pessoa(), 6)

    def test_bolo_chocolate(self):
        self.assertEqual(self.bolo_chocolate.bolo(), "Bolo de Cenoura e chocolate")
        self.assertEqual(self.bolo_chocolate.pessoa(), 11)

    def test_bolo_nata(self):
        self.assertEqual(self.bolo_nata.bolo(), "Bolo de Cenoura e chocolate, nata e morango")
        self.assertEqual(self.bolo_nata.pessoa(), 14)


if __name__ == "__main__":
    unittest.main()