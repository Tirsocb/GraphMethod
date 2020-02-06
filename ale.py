import re

a=25
b=33.33

m="6x+9y<=450"
n="10x+9y<=550"
z="85x+115y"

def c1(z):
    a=int(re.findall(r"(\d+)y", z)[0])
    return a
    
    
def c2(z):
    a=int(re.findall(r"(\d+)z", z)[0])
    return b

def slope(r): #Encontrar la pendiente de una restriccion
    a=int(re.findall(r"(\d+)x", r)[0]) #le asigna a la variable el numero que se encuentra antes de la x
    b=int(re.findall(r"(\d+)y", r)[0])
    if (a==0): #devuelve una pendiente =0 automaticamente si no hay ninguna y
        return a
    elif (b==0): #evita que se hagan divisiones dentro de 0
        return b
    elif(a,b >0): 
        return a/b

def intervalc1(r1,r2,obj): #encuentra el intervalo en el que puede variar c1
    slope1=slope(r1)*c1(obj) #multiplica la pendiente de la primera restriccion, por la pendiente de la funcion objetivo, para despejar c1
    slope1 = str(round(slope1, 2))
    slope2=slope(r2)*c1(obj)
    slope2 = str(round(slope2, 2))
    resultado=(25*slope1)+(b*115)
    return ("C1 puede variar entre"+str(slope1)+" y "+str(slope2))
    
print(intervalc1(m,n,z))

