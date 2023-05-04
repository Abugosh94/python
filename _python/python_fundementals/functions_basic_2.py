#Countdown

def cd(x):
    a=[]
    while (x>=0):
        a.append(x)
        x-=1
    return a

#Print and return

def par(x):
    print (x[0])
    return x[1]

#First plus length

def fpl(x):
    return x[0]+len(x)

#Values greater than second

def vgts(x):
    values =[]
    for i in range(0, len(x), 1):
        if(x[i]>x[1]):
            values.append(x[i])
    print (len(values))

    if(len(x)>2):
        return values
    else:
        return False


#This length, that value

def tltv(x, y):
    result = []
    for i in range(0, x, 1):
        result.append(y)

    return result