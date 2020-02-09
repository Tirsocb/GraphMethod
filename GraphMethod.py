from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

x, y = sp.symbols('x y')
# poner coeficientes de la funcion objetivo
arrobj = [4, 3, 0, 0]
# coefeicientes y limite de las restricciones, el ultimo spot del array es el signito de mayor o menor a
restrict1 = [4, 2, 60, '<']
restrict2 = [2, 4, 48, '<']

# poner funciones y restricciones en formato de sympy
funcion_objetivo = Eq(arrobj[0] * x + arrobj[1] * y)
restriccion1 = Eq(restrict1[0] * x + restrict1[1] * y, restrict1[2])
restriccion2 = Eq(restrict2[0] * x + restrict2[1] * y, restrict2[2])

# matriz
fila1 = [restrict1[0], restrict1[1], restrict1[2]]
fila2 = [restrict2[0], restrict2[1], restrict2[2]]

arrayPuntosCandidatos = []


# funcion para verificar que los coeficientes de las restricciones cumplan con las restricciones
def puntosCandidatos(x, y):
    testvar = True

    # restriccion 1
    if restrict1[3] == '<':
        if restrict1[0] * x + restrict1[1] * y <= restrict1[2]:
            pass
        else:
            testvar = False
    else:
        if restrict1[0] * x + restrict1[0] * y >= restrict1[2]:
            pass
        else:
            testvar = False

    # restriccion 2
    if restrict2[3] == '<':
        if restrict2[0] * x + restrict2[1] * y <= restrict2[2]:
            pass
        else:
            testvar = False
    else:
        if restrict2[0] * x + restrict2[1] * y >= restrict2[2]:
            pass
        else:
            testvar = False
    # si si cumplen las restricciones meter los puntos a un array
    if testvar == True:
        arrayPuntosCandidatos.append((x, y))
    return testvar


# recibir puntos y asignarlos a la variable correspondiente, dependiendo del largo del array respuesta
def possibleValues(respuesta):
    arrayVar = [v for v in respuesta.values()]
    xx = arrayVar[0]
    yy = arrayVar[1]
    # si las respuestas cumplen con las restricciones ponerlos en el formato adecuadio
    if puntosCandidatos(xx, yy):
        return [arrobj[0] * xx + arrobj[1] * yy, (xx, yy)]
    else:
        return [0, (xx, yy)]  # si no cumplen con las restricciones se devuelve por default 0


# resolver problema, recibe las dos filas de la matriz con los coeficientes y 'x' y 'y' como simbolos de sympy
def solve(f1, f2, x, y):
    soln = Matrix((fila1, fila2))  # declarar matriz sympy

    possiblesoln = possibleValues(solve_linear_system(soln, x, y))  # resolver sistema de ecuaciones para encontrar la
    # interseccion entre restricciones, verificar que el punto cumple y se mete en la variable possiblesoln como una
    # posible solucion al problema

    produccionMax = 0
    # probar que la solucion sea la indicada para maximizar la funcion objetivo
    if possiblesoln[0] > produccionMax and possiblesoln[1] in arrayPuntosCandidatos:
        produccionMax = possiblesoln[0]
        puntoMax = possiblesoln[1]
    # se devuelve el punto que maximiza 
    return puntoMax


print(solve(fila1, fila2, x, y))
