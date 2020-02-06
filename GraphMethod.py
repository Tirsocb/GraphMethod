from sympy import Eq, solve_linear_system, Matrix
import sympy as sp

x, y = sp.symbols('x y')
# poner coeficientes de la funcion objetivo
arrobj = [1091, 1411, 0, 0]
# coefeicientes y limite de las restricciones, el ultimo spot del array es el signito de mayor o menor a
restrict1 = [8, 12, 600, '<']
restrict2 = [5, 10, 450, '<']
restrict3 = [2, 2, 140, '<']
funcion_objetivo = Eq(arrobj[0] * x + arrobj[1] * y)
restriccion1 = Eq(restrict1[0] * x + restrict1[1] * y, restrict1[2])
restriccion2 = Eq(restrict2[0] * x + restrict2[1] * y, restrict2[2])
restriccion3 = Eq(restrict3[0] * x + restrict3[1] * y, restrict3[2])

# matriz
fila1 = [restrict1[0], restrict1[1], restrict1[2]]
fila2 = [restrict2[0], restrict2[1], restrict2[2]]
fila3 = [restrict3[0], restrict3[1], restrict3[2]]

arrayPuntosCandidatos = []


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

    # restriccion 3
    if restrict3[3] == '<':
        if restrict3[0] * x + restrict3[1] * y <= restrict3[2]:
            pass
        else:
            testvar = False
    else:
        if restrict3[0] * x + restrict3[1] * y >= restrict3[2]:
            pass
        else:
            testvar = False

    if testvar == True:
        arrayPuntosCandidatos.append((x, y))
    return testvar


def funcionObjetivo(respuesta):
    arrayVar = [v for v in respuesta.values()]
    xx = arrayVar[0]
    yy = arrayVar[1]

    if puntosCandidatos(xx, yy):
        return [arrobj[0] * xx + arrobj[1] * yy, (xx, yy)]
    else:
        return [0, (xx, yy)]


sol1 = Matrix((fila2, fila3))
sol2 = Matrix((fila1, fila2))
sol3 = Matrix((fila1, fila3))

solve_linear_system(sol1, x, y)
solve_linear_system(sol2, x, y)
solve_linear_system(sol3, x, y)

possiblesol1 = funcionObjetivo(solve_linear_system(sol1, x, y))
possiblesol2 = funcionObjetivo(solve_linear_system(sol2, x, y))
possiblesol3 = funcionObjetivo(solve_linear_system(sol3, x, y))


produccionMax = 0
if possiblesol1[0] > produccionMax and possiblesol1[1] in arrayPuntosCandidatos:
    produccionMax = possiblesol1[0]
    puntoMax = possiblesol1[1]
elif possiblesol2[0] > produccionMax and possiblesol2[1] in arrayPuntosCandidatos:
    produccionMax = possiblesol2[0]
    puntoMax = possiblesol2[1]
elif possiblesol3[0] > produccionMax and possiblesol3[1] in arrayPuntosCandidatos:
    produccionMax = possiblesol3[0]
    puntoMax = possiblesol3[1]

print(puntoMax)
print(produccionMax)

