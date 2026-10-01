import string
import random


def genPop(n,lenWord):
    x = []
    y = []
    z = []

    #lenWord = int(input("Length of each Word?:  ")) #length of each word
    #n = int(input("No. of Words?:  ")) #population
    a = ''

    chars = string.ascii_lowercase + " "

    for i in range(n):
        x.append(random.choices(chars, k=lenWord))

    for i in x:
        for j in i:
            y.append(j)


    for g in range(n):
        for i in range(lenWord): #0,1,2,3 indices
            a+=y[i]
        z.append(a)
        a = ''
        del y[0:lenWord]

    return z

def fitFunc(trgt, pop):

    tlist = []
    for i in trgt:
        tlist.append(i)#tlist = ['r','i','s','h','i']

    idx = 0
    tempFitness = 0
    fitness = []
    tempList = []

    for j in pop: #['mfkds', 'jdoie', ... 'idhuf'] we choose each word
        for h in j:#E.G. the first one -> 'mfkds' we choose each letter, here h == 'm'
            #now we check if each letter in place of the target we have chosen is the same as the letter in place of the word we are iterating.
            tempList.append(h)
        for i in tempList:
            if i == tlist[idx]:
                tempFitness += 1
            idx += 1
        fitness.append(tempFitness)
        tempFitness=0
        idx = 0
        tempList=[]

    return fitness


target = str(input("Target: ")) #str you want to predict

initPop = genPop(10000, len(target))

#fakePop = ['rishi', 'rivyb', 'kkkkk']

#print(initPop)
print(fitFunc(target, initPop))
