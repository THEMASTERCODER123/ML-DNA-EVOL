#By Rishi Dharewa
import string
import random
from collections import Counter

def genRandWord(length):
    x = ''
    chars = string.ascii_letters + " "
    for i in range(length):
        x.append(random.choices(chars, k=length))

def randomCharacter(typeStr):
    if typeStr == "lower":
	    character = random.choice(string.ascii_lowercase + " ")
	    return character
    elif typeStr == "upper":
        character = random.choice(string.ascii_uppercase + " ")
        return character
    elif typeStr == "letters":
        character = random.choice(string.ascii_letters + " ")
        return character
    elif typeStr == "digts":
        character = random.choice(string.digits + " ")
        return character
    elif typeStr == "punctuations":
        character = random.choice(string.punctuation + " ")
        return character
    else:
        character = random.choice(string.ascii_letters + string.digits + string.punctuation + " ")
        return character

def is_even(number):
    return number % 2 == 0
    x = []
    y = []
    z = []

    #lenWord = int(input("Length of each Word?:  ")) #length of each word
    #n = int(input("No. of Words?:  ")) #population
    a = ''

    chars = randomCharacter(typeStr)

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

def genPop(n, lenWord, typeStr):
    population = []
    for i in range(n):
        word = ''
        for j in range(lenWord):
            word += randomCharacter(typeStr)
        population.append(word)
    return population

def fitFunc(trgt, pop, presentBonus):

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
        remainingTarget = Counter(trgt)
        for i in tempList:
            if remainingTarget[i] > 0:
                tempFitness += presentBonus
                remainingTarget[i] -= 1    
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

def topPopProbabilistic1(currentPop, currentFitness, maxAttempts):
    #hash_fitness = dict(zip(currentPop, currentFitness))
    #sorted_hash_fitness = dict(sorted(hash_fitness.items(), key=lambda item: item[1]))
    #fitness_values_list = list(hash_fitness.values())
    totalFitness = 0
    
    for i in currentFitness:
        totalFitness += int(i)

    if totalFitness == 0:
        newTopPop = []

        for i in range(len(currentPop) // 2):

            currentTopPop = random.sample(currentPop, k=2)

            newTopPop.append(currentTopPop)

        return newTopPop

    
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
            attempts =0
            while currentTopPop[0] == currentTopPop[1] and attempts<maxAttempts:
                currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )
                attempts+=1

            newTopPop.append(currentTopPop)
        
    else:
        for i in range((len(currentPop)+1)//2):
            currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )
            attempts =0
            while currentTopPop[0] == currentTopPop[1] and attempts < maxAttempts:
                currentTopPop = random.choices(
                values,
                weights=probabilities,
                k=2
            )
                attempts += 1


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
        if len(pair[0]) == 1:
            words.append(''.join(pair[0]))
            words.append(''.join(pair[1]))
        else:
            for i in range(len(pair[0]) - 1):
                word = pair[0][:i + 1] + pair[1][i+1:]
                words.append(''.join(word))

    return words

def checkTarget(population, target):
    if target in population:
        return True
    else:
        return False
    print("Generation: ", generation)

def mutatePop(currentPop, mutationRate, typeStr):
    mutatedPop = []

    for i in currentPop:
        word = list(i)

        for j in range(len(word)):
            if random.random() < mutationRate:
                word[j] = randomCharacter(typeStr)

        mutatedPop.append(''.join(word))

    return mutatedPop

def selectPopProbabilistic(currentPop, currentFitness, selectionSize):
    totalFitness = 0

    for i in currentFitness:
        totalFitness += int(i)

    if totalFitness == 0:
        return random.choices(currentPop, k=selectionSize)

    normalizedFitness = []

    for i in currentFitness:
        normalizedFitness.append(i / totalFitness)

    newPop = random.choices(
        currentPop,
        weights=normalizedFitness,
        k=selectionSize
    )

    return newPop

def run():
    target = str(input("Target: ")) #str you want to predict
    #target="a"
    typeStr = "lower"
    selection_size_init = 1000
    selection_size_reduction = 1000 #ssi>=ssr
    initPop = genPop(selection_size_init, len(target), typeStr)
    currentPop = initPop
    generation = 1
    maxAttempts = 10
    presentBonus = presentBonus = 0.2 / len(target)

    if len(target) < 5:
        mul_const = 15
    elif len(target) < 10:
        mul_const = 10
    elif len(target) < 15:
        mul_const = 7
    elif len(target) < 20:
        mul_const = 5
    elif len(target) < 30:
        mul_const = 4
    elif len(target) < 40:
        mul_const = 3
    elif len(target) < 50:
        mul_const = 2.5
    elif len(target) < 60:
        mul_const = 2
    elif len(target) < 75:
        mul_const = 1.5
    elif len(target) < 100:
        mul_const = 1.25
    elif len(target) < 150:
        mul_const = 1
    elif len(target) < 250:
        mul_const = 0.8
    elif len(target) < 500:
        mul_const = 0.6
    else:
        mul_const = 0.5

    mutation_rate=1/(mul_const*len(target))
    #mutation_rate = 0.005

    noOfIndiv = 1
    while True:
        x = checkTarget(currentPop, target)
        if x == True:
            if generation == 1:
                print(f'Target Reached: {target}, it was present in the first population.')
                break
        currentFitness = fitFunc(target, currentPop, presentBonus)
        currentTopPop = topPopProbabilistic1(currentPop, currentFitness, maxAttempts)

        crossedPop = cross(currentTopPop, "genAll")
        mutatedPop = mutatePop(crossedPop, mutation_rate, typeStr)

        mutatedFitness = fitFunc(target, mutatedPop,presentBonus)
        currentPop = selectPopProbabilistic(mutatedPop, mutatedFitness, selection_size_reduction)

        for i in currentPop:
            #print("Generation:", generation, "Individual:", i)
            print(f'Generation #{generation}====Individual #{noOfIndiv}:--->{i}\n')
            noOfIndiv += 1
            
            if i == target:
                break
        x = checkTarget(currentPop, target)
        if x == True:
            break
        generation += 1

if __name__ == '__main__':
    run()

'''
    ---------------------------------------------------------------------------------------
initPop = genPop(10000, len(target))
initFitness = fitFunc(target, initPop)
initTopPop = topPopProbabilistic1(initPop, initFitness)
initCross = cross(initTopPop, "genAll")
    ---------------------------------------------------------------------------------------
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

