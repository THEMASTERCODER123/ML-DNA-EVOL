import random
import string

x = []
y = []
z = []

lenWord = int(input("Length of each Word?:  ")) #length of each word
n = int(input("No. of Words?:  ")) #no. of elements
a = ''

chars = string.ascii_letters + " "

for i in range(n):
    x.append(random.choices(chars, k=lenWord))

for i in x:
    for j in i:
        y.append(j)

print("list y initial",y)

for g in range(n):
    for i in range(lenWord): #0,1,2,3 indices
        a+=y[i]
    z.append(a)
    a = ''
    del y[0:lenWord]


print("List x: ",x)
print("List y final: ",y)
print("list z: ",z)