import re

#Este formato de restricciones y funcion objetivo se utiliza para el analisis de sensibilidad
r1="4x+8y<=480"
r2="5x+6y<=600"
r3="12x+8y<=540"
obje="100x+120y"

def c1(z):
    a=int(re.findall(r"(\d+)y", z)[0])
    return a
    
def c2(z):
    a=int(re.findall(r"(\d+)x", z)[0])
    return a

print(c2(obje))    

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
    i = slope1
    while i <= slope2:
        tuplaoriginal=(15/2, 225/4)
        #tuplaprueba = method() #Aqui hace la maximizacion y compara si sigue igual que la original
        if (cmp(tuplaoriginal,tuplaprueba)==0):
            i += 0.01
        else(cmp(tuplaoriginal,tuplaprueba)!=0):
            i=slope2
            return ("C1 no puede variar entre ("+str(slope1)+","+str(slope2)+")")
    
    if(i==(slope2)):
        return ("C1 puede variar entre ("+str(slope1)+","+str(slope2)+")")

def intervalc2(r1,r2,obj):
    slope1=float(format(slopec2(r1)*c2(obj),'.2f')) 
    slope2=float(format(slopec2(r2)*c2(obj),'.2f'))
    i = slope2
    while i < slope1:
        tuplaoriginal=(15/2, 225/4)
        #tuplaprueba = method() #Aqui hace la maximizacion y compara si sigue igual que la original
        if (cmp(tuplaoriginal,tuplaprueba)==0):
            i += 0.01
        else(cmp(tuplaoriginal,tuplaprueba)!=0):
            i=slope2
            return ("C2 no puede variar entre ("+str(slope2)+","+str(slope1)+")")
    
    if(i==(slope1)):
        return ("C2 puede variar entre ("+str(slope2)+","+str(slope1)+")")
    


