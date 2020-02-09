from sympy import Eq, solve_linear_system, Matrix
import sympy as sp
import re


x, y = sp.symbols('x y')
# poner coeficientes de la funcion objetivo
arrobj = [4, 3, 0, 0]
# coefeicientes y limite de las restricciones, el ultimo spot del array es el signito de mayor o menor a
restrict1 = [4, 2, 60, '<']
restrict2 = [2, 4, 48, '<']

#Este formato de restricciones y funcion objetivo se utiliza para el analisis de sensibilidad
r1="4x+2y<=60"
r2="2x+4y<=48"
obje="4x+3y"

'''RESOLUCION METODO GRAFICO'''

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

#solve(fila1, fila2, x, y)

''' ANALISIS DE SENSIBILIDAD '''

def c1(z):
    a=int(re.findall(r"(\d+)y", z)[0])
    return a
    
def c2(z):
    a=int(re.findall(r"(\d+)x", z)[0])
    return a  

def slope(r): #Encontrar la pendiente de una restriccion
    a=int(re.findall(r"(\d+)x", r)[0]) #le asigna a la variable el numero que se encuentra antes de la x
    b=int(re.findall(r"(\d+)y", r)[0])
    if (a==0): #devuelve una pendiente =0 automaticamente si no hay ninguna y
        return a
    elif (b==0): #evita que se hagan divisiones dentro de 0
        return b
    elif(a,b >0): #si hay x,y devuelve la pendiente de estas
        return a/b

#Para sacar r2 es necesario encontrar las pendientes inversas de las restricciones, casi es lo mismo, pero se dividen al reves
def slopec2(r): 
    a=int(re.findall(r"(\d+)x", r)[0]) 
    b=int(re.findall(r"(\d+)y", r)[0])
    if (a==0): 
        return a
    elif (b==0): 
        return b
    elif(a,b >0): 
        return b/a #inversa

def intervalc1(r1,r2,obj): #encuentra el intervalo en el que puede variar c1
    slope1=float(format(slope(r1)*c1(obj),'.2f')) #multiplica la pendiente de la primera restriccion, por la pendiente de la funcion objetivo, para despejar c1
    slope2=float(format(slope(r2)*c1(obj),'.2f'))
    i = slope2 #le asigna el valor de la pendiente en el rango minimo para comenzar a probar
    tuplaoriginal=solve(fila1, fila2, x, y) #resuelve con los valores originales 
    while i < slope1: #En este while se prueba todos los posibles valores que podria tomar la x
        arrobj[0] = i #Cambia el valor de la x en la funcion objetivo de 0.01 en 0.01
        tuplaprueba = solve(fila1, fila2, x, y) #Aqui hace la maximizacion con el nuevo valor 
        if (tuplaoriginal==tuplaprueba): #hace la comparacion entre tuplas
            i=i+0.01
            i=float("{0:.2f}".format(i)) #le da un formato de 2 decimales, esto lo definimos asi ya que estamos hablando de precios
        elif(tuplaoriginal!=tuplaprueba):
            i=slope2
            return ("C1 no puede variar entre ("+str(slope2)+","+str(slope1)+")") 
    
    if(i==(slope1)):
        return ("C1 puede variar entre ("+str(slope2)+","+str(slope1)+")")

def intervalc2(r1,r2,obj): #basicamente hace lo mismo pero para encontrar c2, es decir, los posibles valores de y
    slope1=float(format(slopec2(r1)*c2(obj),'.2f')) 
    slope2=float(format(slopec2(r2)*c2(obj),'.2f'))
    i = slope1 #solo intercambia slope 1 por slope 2
    tuplaoriginal=solve(fila1, fila2, x, y)
    while i < slope2:
        arrobj[1] = i
        tuplaprueba = solve(fila1, fila2, x, y)
        if (tuplaoriginal==tuplaprueba):
            i=i+0.01
            i=float("{0:.2f}".format(i))
        elif(tuplaoriginal!=tuplaprueba):
            i=slope2
            return ("C2 no puede variar entre ("+str(slope1)+","+str(slope2)+")")
    
    if(i==(slope2)):
        return ("C2 puede variar entre ("+str(slope1)+","+str(slope2)+")")
    
print(solve(fila1, fila2, x, y))
print(intervalc1(r1,r2,obje))
print(intervalc2(r1,r2,obje))
