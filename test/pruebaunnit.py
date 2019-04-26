import unittest
from funciones import functions

class TestCollectionMethods(unittest.TestCase):

 def test_invertir(self):

  lista = (2, 3, 4, 5, 6)

  result1 = functions.invertir(lista)
  self.assertEqual(result1, (6, 5, 4, 3, 2))

