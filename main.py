#By Rishi Dharewa
import string
import random

def is_even(number):
    return number % 2 == 0

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

def topPopElitist(currentPop, currentFitness):
    hash_fitness = dict(zip(currentPop, currentFitness))
    sorted_hash_fitness = dict(sorted(hash_fitness.items(), key=lambda item: item[1]))

    if is_even(len(sorted_hash_fitness)) == True:
        midpoint_idx = (len(sorted_hash_fitness))/2 #where top 50% starts
    #elif is_even(len(sorted_hash_fitness)) == False:
    else:
        midpoint_idx = ((len(sorted_hash_fitness)+1)/2)-1 #where top 50% starts
    
    target_idx = int(midpoint_idx - 1)

    keys_to_remove = list(sorted_hash_fitness.keys())[:target_idx + 1]

    for key in keys_to_remove:
        del sorted_hash_fitness[key]

    return sorted_hash_fitness

def topPopProbabilistic1(currentPop, currentFitness):
    #hash_fitness = dict(zip(currentPop, currentFitness))
    #sorted_hash_fitness = dict(sorted(hash_fitness.items(), key=lambda item: item[1]))
    #fitness_values_list = list(hash_fitness.values())
    totalFitness = 0
    for i in currentFitness:
        totalFitness += int(i)

    if totalFitness == 0:
        totalFitness = 1
    
    normalizedFitness = []

    for i in currentFitness:
        normalizedFitness.append(i/totalFitness)

    #hash_normalized_fitness = dict(zip(currentPop, normalizedFitness))

    #probabilities = list(hash_normalized_fitness.values())
    #values = list(hash_normalized_fitness.keys())
    
    values = currentPop
    probabilities = normalizedFitness

    newProbabilities = []

    '''for i in probabilities:
        newProbabilities.append(float(i))'''

    newTopPop = []
    if len(currentPop)%2==0:
        for i in range(len(currentPop)//2):
            currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )

            while currentTopPop[0] == currentTopPop[1]:
                currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )

            newTopPop.append(currentTopPop)
        
    else:
        for i in range((len(currentPop)+1)//2):
            currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )
            while currentTopPop[0] == currentTopPop[1]:
                currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )
            newTopPop.append(currentTopPop)


    return newTopPop


def cross(currentTopPop, method):
    tl = []
    pl=[]

    if method == "5050":
        return 0
    elif method == "genAll":
        for pair in currentTopPop: # 'pair' looks like ['rishi', 'rivyb']
                parent1 = list(pair[0]) # Result: ['r', 'i', 's', 'h', 'i']
                parent2 = list(pair[1]) # Result: ['r', 'i', 'v', 'y', 'b']
                tl.append([parent1, parent2])
    words=[]
    for pair in tl:
        for i in range(len(pair[0]) - 1):
            word = pair[0][:i + 1] + pair[1][i:-1]
            words.append(''.join(word))

    return words, len(words)




target = str(input("Target: ")) #str you want to predict

initPop = genPop(10000, len(target))
initFitness = fitFunc(target, initPop)
initTopPop = topPopProbabilistic1(initPop, initFitness)
initCross = cross(initTopPop, "genAll")

print(initCross)


'''
    Testing:-
    fakePop = ['rishi', 'rivyb', 'kkkkk']
    ---------------------------------------------------------------------------------------

    #To check for no. of iterations before generation of target (in init population)

    cout = 0
    while max(fitFunc(target, initPop)) != len(target):
        print(fitFunc(target, initPop))
        print(max(fitFunc(target, initPop)))
        cout += 1
        print(f'No of iterations is {cout}')
    ---------------------------------------------------------------------------------------

    #to check for max fit individual

    g = fitFunc(target, initPop)
    f = max(g)
    print(f'Fitness: {f}')
    print(f'Relative Fitness: {f/len(target)}')
    print(f'Index of max fitness is: {g.index(f)}')
    print(f'The max fit individual is: {initPop[g.index(f)]}')
    ---------------------------------------------------------------------------------------
'''

