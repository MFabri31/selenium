import unittest

class UnittestMethods(unittest.TestCase):
    @classmethod # el método se ejecuta a nivel de clase (solo una vez)
    def setUpClass(cls):
        print("Inicio cuando empieza la clase")


    def setUp(self):
        """Define las precondiciones antes de iniciar cada tc. prepara el contexto"""
        print("Inicio en cada test case")

    
    def test_message(self):
        print("Test case de mensaje")


    def test_number(self):
        print("Test case de número")


    def tearDown(self):
        """Destruye el contexto"""
        print("Finaliza la ejecución de cada uno de los test cases")


    classmethod
    def tearDownClass(self):
        print("Inicio cuando finaliza la clase")


if __name__ == "__main__":
    unittest.main()