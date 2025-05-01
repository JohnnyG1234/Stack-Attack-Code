import fileinput


# A normal function
def getPi():
    with open("pi.txt", "r") as file:
        return [line.rstrip() for line in file]



#print(getPi())
    





# A generator
def piGenerator():
    with open("pi.txt", "r") as file:
        for line in file:
            yield line.rstrip()
    


genPi = piGenerator()

print(next(genPi))
print(next(genPi))
print(next(genPi))
print(next(genPi))
print(next(genPi))



