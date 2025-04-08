from collections import defaultdict

numbers = enumerate([1, 2, 3, 4, 5])
print(list(numbers))
for i,num in numbers:
    print(i,num)

squares = [x ** 2 for x in range(10)] # list en comprehension
ssquares = {x ** 2 for x in range(10)} # set en comprehension
dsquares = {str(x):x ** 2 for x in range(10)} # set en comprehension

gsquares = (x ** 2 for x in range(10)) # ???

print(squares)
print(ssquares)
print(dsquares)

print(gsquares)
print(list(gsquares))

# unpacking
name,_,salaire = ("fred",20, 10000000000000000)
print(name)

a,*b,_ = [1,2,3,4,5,6]
print(b)


data = [1,2.0,3,4,5,6,True,"Help",5.55]

print(data[4:1:-1])
print(data[::-2])
print(data[-1]) # print(data[len(data)-1])

# zip
names = ["Alice", "Bob", "Charlie", "Fred"]
ages = [25, 30, 35]

z = list(zip(names, ages))
print(z)
for name, age in z: # unpack
    print(f"{name} has {age} years old")

d = defaultdict(str)
dic1 = {1:"one",2:"two"}
d[1] = "one"
d[2] = 2

print(d[3])


dico1 = {}
surprise = {1,2,3}
dicosurprise = {1:1,2:4,3:9}

# liste en comprehension
racinecarrees = [  x ** 0.5 for x in range(100) ]
# dict en comprehension
dicoracinecarrees = {  x:x**0.5 for x in range(100) }
# set en comprehension
setracines = { x**0.5 for x in range(100) }

s = set()
d= dict()

print(dicoracinecarrees)

a,b = 10,21
a,b = b,a #unpack

print(a,b)


names = ["Alice", "Bob", "Charlie","Gabriel"]
ages = [25, 30, 35]

zz = zip(names, ages)
for name, age in zz:
    print(f"{name} has {age} years old")


