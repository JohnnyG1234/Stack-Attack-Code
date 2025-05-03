import os.path

REAL_FILE_PATH = "text.txt"
FAKE_FILE_PATH = "fake.txt"

os.path.isfile(REAL_FILE_PATH)

def methodOne():
    try:
        file = open(REAL_FILE_PATH)
        print(file.read())
    except FileNotFoundError:
        print("file not found!")
    
    try:
        file = open(FAKE_FILE_PATH)
        print(file.read())
    except FileNotFoundError:
        print("file not found!")


def causesException():
    file = open(FAKE_FILE_PATH)



def withoutTry():
    if os.path.isfile(REAL_FILE_PATH):
        file = open(REAL_FILE_PATH)
        print(file.read())
    else:
        print("file not found!")
    

    if os.path.isfile(FAKE_FILE_PATH):
        file = open(FAKE_FILE_PATH)
        print(file.read())
    else:
        print("file not found!")


def whatCouldGoWrong():
    path = "text.txt"

    if not os.path.isfile(path):
        return

    # something silly happens!
    # file gets deleted or....
    path = "junk.txt"

    file = open(path)
    print(file.read())





if __name__ == "__main__":
    #methodOne()
    #withoutTry()
    #causesException()
    whatCouldGoWrong()