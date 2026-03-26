'''a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)

i=[i for i in range(1,100) if i%2==0]
'''
#List Comprehension
#Lamda Function

#Generator Expression
def reels():
    r = ['1..100','101..200','201..300','301..400','401..500']
    for i in r:
        yield i

scroll = reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
