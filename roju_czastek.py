from random import *
def SwarmMax():

    c1=0.4
    c2=0.5
    w=0.3

    maxIteracji=500

    min=-10
    max=10
    nmin=-abs(max-min)
    nmax=abs(max-min)
    n=5 #liczba czastek
    d=2 #dimension

    #x = [[(min+random()*(max-min) )for i in range(d)] for j in range(n)] #pierwsze pozycje roju
    #v=[[(min+random()*(max-min) )for i in range(d)] for j in range(n)] # predkosci ????? czy dobry zakres
    x = [[(uniform(min,max) )for i in range(d)] for j in range(n)] #pierwsze pozycje roju
    v=[[(uniform(nmin,nmax) )for i in range(d)] for j in range(n)] # predkosci ????? czy dobry zakres
    
    p=x #najlepsza pozycja dla kazdej cząstki
    p_wartosci=[0]*n #najlepsza wartosc dla kazdej cząstki
    
    bestWartosc=FunkcjaFitness(x[0]) #wartosc 
    bestPozycja=x[0] #wektor pozycja najlepszej cząstki
    
    for i in range(n):
        fit=FunkcjaFitness(x[i])
        p_wartosci[i]=fit
        if fit>bestWartosc:
            bestWartosc=fit
            bestPozycja=x[i]
    
    t=0
    while t<maxIteracji:
        for i in range(n):
            for j in range(d):
                r1=random()
                r2=random()
                v[i][j]=w*v[i][j]+c1*r1*(p[i][j]-x[i][j])+c2*r2*(bestPozycja[j]-x[i][j])
                x[i][j]=x[i][j]+v[i][j]
            fit=FunkcjaFitness(x[i])
            print(fit,p_wartosci)
            if fit>p_wartosci[i]:
                p_wartosci[i]=fit
                p[i]=x[i]
                if fit>bestWartosc:
                    bestWartosc=fit
                    bestPozycja=x[i]
        t+=1


    print("Najwieksza wartosc funkcji to: ", bestWartosc,", na pozycji: ",bestPozycja)
    return
def SwarmMin():

    c1=0.3
    c2=0.5
    w=0.3

    maxIteracji=500

    min=-10
    max=10
    nmin=-abs(max-min)
    nmax=abs(max-min)
    n=5 #liczba czastek
    d=2 #dimension

    x = [[(min+random()*(max-min) )for i in range(d)] for j in range(n)] #pierwsze pozycje roju
    v=[[(nmin+random()*(nmax-nmin) )for i in range(d)] for j in range(n)] # predkosci ????? czy dobry zakres
    
    p=x #najlepsza pozycja dla kazdej cząstki
    p_wartosci=[0]*n #najlepsza wartosc dla kazdej cząstki
    
    bestWartosc=FunkcjaFitness(x[0]) #wartosc 
    bestPozycja=x[0] #wektor pozycja najlepszej cząstki
    
    for i in range(n):
        fit=FunkcjaFitness(x[i])
        p_wartosci[i]=fit
        if fit<bestWartosc:
            bestWartosc=fit
            bestPozycja=x[i]
    
    t=0
    while t<maxIteracji:
        for i in range(n):
            for j in range(d):
                r1=random()
                r2=random()
                v[i][j]=w*v[i][j]+c1*r1*(p[i][j]-x[i][j])+c2*r2*(bestPozycja[j]-x[i][j])
                x[i][j]=x[i][j]+v[i][j]
            fit=FunkcjaFitness(x[i])
            if fit<p_wartosci[i]:
                p_wartosci[i]=fit
                p[i]=x[i]
                if fit<bestWartosc:
                    bestWartosc=fit
                    bestPozycja=x[i]
        t+=1


    print("Najmniejsza wartosc funkcji to: ", bestWartosc,", na pozycji: ",bestPozycja)
    return


def FunkcjaFitness(x):
    sum=0
    #sphere
    for i in x:
        sum+=i**2
    

    #Styblinski
    #for i in x:
     #   sum+=i**4-16*i**2+5*i
    #sum=sum/2
    return sum
    

SwarmMin()