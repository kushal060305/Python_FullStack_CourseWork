'''def display(n):
    if n>10:
        return

    display(n+1)
    print(n)

display(1)
'''

def dispaly(n):
    n+=(8,9)
    print("Inside ",n)

n=(1,2,3,4,5,6,7)
dispaly(n)
print("Outside ",n)
