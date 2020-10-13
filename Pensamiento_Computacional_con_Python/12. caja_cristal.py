import unittest

def esmayordeedad (edad):
    if edad >= 18:
        return True
    else:
        return False

def esmenordeedad (edad):
    if edad < 18:
        return True
    else:
        return False

class pruebasdecristaltest (unittest.TestCase):
    def testmayordeedad(self):
        edad=20

        resultado =esmayordeedad(edad)

        self.assertEqual(resultado,True)

    def testmenordeedad(self):
        edad=17
        resultado= esmenordeedad(edad)

if __name__=='__main__':
    unittest.main()