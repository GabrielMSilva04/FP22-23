def read_list(fname):
    nameList = [line.rstrip() for line in open(fname)]
    return nameList[1:]

def apelido(namelist):
    dic = {}
    lst = [name.split(" ") for name in namelist]
    for name in lst:
        for (firstName, *_, lastName) in lst:
            if lastName not in dic:
                dic[lastName] = {firstName}
            else:
                dic[lastName].add(firstName)
    return dic


print(apelido(read_list("Aula08/names.txt")))