

def main():
    num = 5

    isEven = True if num % 2 == 0 else False
    
    print(f'setting to var: {isEven}')
    print(" ")
    print(f'return from func: {isEvenFunc(num)}')


def isEvenFunc(num):
    return True if num % 2 == 0 else False


# this code but in C# 
# bool isEven = (num % 2 == 0) ? true : false;


if __name__ == "__main__":
    main()