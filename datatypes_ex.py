#ListExample

names=["shravan","sandeep","praful","rakesh","vijay"]
print(names)

#print value from a list by using index nos
print(names[1])
print(names[-3])

#updating a single str
names[-3]="savan"
print(names)

#updating multiple string's
a="arun","varun"
names[-4]=a
print(names)

#append
names.append("sandeep")
print(names)

#insert
names.insert(6,"preetam")
print(names)

#delete
del names[0]
print(names)

#Tuple
my_tuple=(2,4,6,8,10,12)
print(my_tuple)

#Set
dic={}
print(type(dic))
set1={}
print(type(set1))

A={1,2,3,4,7,9}
B={2,10,5,9,11,12,13,14}

#union
C=A.union(B)
print(C)
a={1,2,3,4}
a.add(20)
print(a)
C=A|B|a
print(C)

#intesection_set
C=A&B
print(C)

C=A&B&a
print(C)

#frozenset
D=frozenset([8,2])
print(D)

#add
D.add(2)
print(D)
