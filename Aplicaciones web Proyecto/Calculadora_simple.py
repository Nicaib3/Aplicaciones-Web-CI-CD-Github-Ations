class Funcion:
    @staticmethod
    def suma(n1, n2):
        print('SE SELECCIONO SUMA')
        suma = n1 + n2
        print('EL RESULTADO DE SU SUMA ES ', suma)
        return suma
    @staticmethod
    def resta(n1, n2):
        print('SE SELECCIONO RESTA')
        resta = n1 - n2
        print('EL RESULTADO DE SU RESTA ES ', resta)
        return resta
    @staticmethod
    def division(n1, n2):
        print('SE SELECCIONO DIVISION')
        if n2 == 0:
            print("NO SE PUEDE DIVIDIR ENTRE CERO")
            return None
        division = n1 / n2
        print('EL RESULTADO DE SU DIVISION ES ', division)
        return division
    @staticmethod
    def multiplicacion(n1, n2):
        print('SE SELECCIONO MULTIPLICACION')
        multiplicacion = n1 * n2
        print('EL RESULTADO DE SU MULTIPLICACION ES ', multiplicacion)
        return multiplicacion

if __name__ == "__main__":
    while True:
        print('\nBIENVENIDO A LA NICAIB-CALCULADORA')
        opcion = input('QUE OPCION DESEA?    1.SUMA   2.RESTA   3.DIVISION   4.MULTIPLICACION   5.SALIR   | -> ')
        if opcion == '5':
            print("¡Adiós!")
            break 
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = int(input('INSERTE EL PRIMER NUMERO: '))
                num2 = int(input('INSERTE EL SEGUNDO NUMERO: ')) 
                if opcion == '1':
                    Funcion.suma(num1, num2)
                elif opcion == '2':
                    Funcion.resta(num1, num2)
                elif opcion == '3':
                    Funcion.division(num1, num2)
                elif opcion == '4':
                    Funcion.multiplicacion(num1, num2)
            except ValueError:
                print("POR FAVOR, INGRESA SOLO NUMEROS VALIDOS.")
        else:
            print('ESA NO ES UNA OPCION VALIDA!')