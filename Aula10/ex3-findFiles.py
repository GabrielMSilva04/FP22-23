import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext):
    # Complete...
    lst=[]
    #lst = [path+"/"+fname for fname in os.listdir(path) if ext in fname]
    for fname in os.listdir(path):
        completepath = path+"/"+fname
        if ext in fname:
            lst.append(completepath)
        if os.path.isdir(completepath):
            lst.extend(findFiles(completepath, ext))
    return lst
            


def main():
    print("Testing printDirFiles('..'):")
    printDirFiles("..")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    print("\nTesting findFiles('..', '.csv'):")
    lst = findFiles("..", ".csv")
    print(lst)

if __name__ == "__main__":
    main()

