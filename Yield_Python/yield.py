
# This is a  generator!
def func():
    yield "Hello"
    yield "World"

# calling that generator
def helloWorld():
    gen = func()
    print(next(gen))
    print(next(gen))


# another  generator
def digitsOfPi():
    pi = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128"

    for digit in pi:
        yield digit

def getDigits(numDigits: int):
    digits = ""
    pi = digitsOfPi()

    for i in range(numDigits):
        digits += next(pi)
    
    return float(digits)

if __name__ == "__main__":
    helloWorld()

    print(getDigits(5))
    print(getDigits(15))
    print(getDigits(1))
