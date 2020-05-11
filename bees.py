from random import *
def FunkcjaCelu(x):
    sum=0
    #sphere
    for i in x:
        sum+=i**2
    return sum
def Wypisz(x):
    print()
    for i in x:
        print(i)
    print()
    return

def RozeslijPoczatkowe(ile,min,max,d):
    scouts=[[min+random()*(max-min)for i in range(d)] for j in range(ile)]
    scoutsAndFitness=[]
    for i in scouts:
        tab=i
        fit=FunkcjaCelu(i)
        tab.append(fit)
        scoutsAndFitness.append(tab)
    scoutsAndFitness=sorted(scoutsAndFitness, key=lambda x:x[d])
    return scoutsAndFitness

def RozesljPojedynczyWymiar(ile,min,max):
    if min<-10:
        min=-10
    if max>10:
        max=10
    nowy=min+random()*(max-min)
    return nowy
def sasiedztwo(ngh,min,max):
    ngh=0.8*ngh
    rozmiarKwiatka=ngh*(max-min)
    return ngh, rozmiarKwiatka

def TaniecMIN(scoutsAndFitness, e,ileNaElite,ileNareszte,ngh,rozmiar):
    d=len(scoutsAndFitness[0])
    elita=[]
    for i in range(e):
        elita.append(scoutsAndFitness[i])
    for i in range(e):
        tab=[]
        robotnice=[]
        for j in range(d-1):
            nmin=elita[i][j]-rozmiar/2
            nmax=elita[i][j]-rozmiar/2
            robotnice.append(RozesljPojedynczyWymiar(ileNaElite,nmin,nmax))
        fit=FunkcjaCelu(robotnice)
        robotnice.append(fit)
        if fit<scoutsAndFitness[i][d-1]:
            scoutsAndFitness[i]=robotnice
    reszta=[]
    m=len(scoutsAndFitness)
    for i in range(m-e):
        reszta.append(scoutsAndFitness[e+i])
    for i in range(len(scoutsAndFitness)-e):
        tab=[]
        robotnice=[]
        for j in range(d-1):
            nmin=reszta[i][j]-rozmiar/2
            nmax=reszta[i][j]-rozmiar/2
            robotnice.append(RozesljPojedynczyWymiar(ileNareszte,nmin,nmax))
        fit=FunkcjaCelu(robotnice)
        robotnice.append(fit)
        if fit<scoutsAndFitness[e+i][d-1]:
            scoutsAndFitness[e+i]=robotnice
    scoutsAndFitness=sorted(scoutsAndFitness, key=lambda x:x[d-1])
    return scoutsAndFitness
def TaniecMAX(scoutsAndFitness, e,ileNaElite,ileNareszte,ngh,rozmiar):
    d=len(scoutsAndFitness[0])
    elita=[]
    for i in range(e):
        elita.append(scoutsAndFitness[i])
    for i in range(e):
        tab=[]
        robotnice=[]
        for j in range(d-1):
            nmin=elita[i][j]-rozmiar/2
            nmax=elita[i][j]-rozmiar/2
            robotnice.append(RozesljPojedynczyWymiar(ileNaElite,nmin,nmax))
        fit=FunkcjaCelu(robotnice)
        robotnice.append(fit)
        if fit>scoutsAndFitness[i][d-1]:
            scoutsAndFitness[i]=robotnice
    reszta=[]
    m=len(scoutsAndFitness)
    for i in range(m-e):
        reszta.append(scoutsAndFitness[e+i])
    for i in range(len(scoutsAndFitness)-e):
        tab=[]
        robotnice=[]
        for j in range(d-1):
            nmin=reszta[i][j]-rozmiar/2
            nmax=reszta[i][j]-rozmiar/2
            robotnice.append(RozesljPojedynczyWymiar(ileNareszte,nmin,nmax))
        fit=FunkcjaCelu(robotnice)
        robotnice.append(fit)
        if fit>scoutsAndFitness[e+i][d-1]:
            scoutsAndFitness[e+i]=robotnice
    scoutsAndFitness=sorted(scoutsAndFitness, key=lambda x:x[d-1],reverse=True)
    return scoutsAndFitness

def Bees():
    ileScoutow=50
    min=-10
    max=10
    ileNaElite=20
    ileNaReszte=10
    ileIteracji=2000
    ngh=0.4
    e=3
    d=2
    scoutsAndFitness=RozeslijPoczatkowe(ileScoutow,min,max,d)
    saf=scoutsAndFitness
    saf=sorted(scoutsAndFitness, key=lambda x:x[d],reverse=True)
    i=0
    while i<ileIteracji:    
        ngh,rozmiar=sasiedztwo(ngh,min,max)
        scoutsAndFitness=TaniecMIN(scoutsAndFitness,e,ileNaElite,ileNaReszte,ngh,rozmiar)
        i+=1
    
    i=0
    while i<ileIteracji:    
        ngh,rozmiar=sasiedztwo(ngh,min,max)
        saf=TaniecMAX(saf,e,ileNaElite,ileNaReszte,ngh,rozmiar)
        i+=1
    print("Wspolrzedne najmnijeszej wartosci i najmniejsza wartosc: ")
    print(scoutsAndFitness[0])

    print("Wspolrzedne najwiekszej wartosci i najwieksza wartosc: ")
    print(saf[0])
print(Bees())