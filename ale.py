import re

m="6x+9y<=450"
n="10x+9y<=550"


def c1(z):
    a=int(re.findall(r"(\d+)y", z)[0])
    
    
def c2(z):
    a=int(re.findall(r"(\d+)z", z)[0])

def slope(r1): #Encontrar la pendiente de una restriccion
    a=int(re.findall(r"(\d+)x", r1)[0]) #le asigna a la variable el numero que se encuentra antes de la x
    b=int(re.findall(r"(\d+)y", r1)[0])
    if (a==0):
        return a
    elif (b==0):
        return b
    
    return -a/b

def interval(r1,r2,obj):
    slope1=slope(r1)
    slope2=slope(r2)
    
    return 'hola'
    
print(slope(m))

