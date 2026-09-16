from Calculadora_simple import Funcion

def test_operaciones_calculadora():
    assert Funcion.suma(5, 3) == 8
    assert Funcion.resta(10, 4) == 6
    assert Funcion.multiplicacion(3, 4) == 12    
    assert Funcion.division(10, 2) == 5