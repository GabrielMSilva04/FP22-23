
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("Aula07/nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for i in lst:
        name = i[NAME]
        volume = i[VOLUME]
        if name not in totVol:
            totVol[name] = volume
        else:
            totVol[name] += volume
    return totVol

def maxValorization(lst):
    vMax = {}
    for i in lst:
        name = i[NAME]
        date = i[DATE]
        value = i[CLOSE]/i[OPEN]*100
        if date not in vMax:
            vMax[date] = (name,str(round(value, 2))+"%")
        elif value > float(vMax[date][1][:-1]):
            vMax[date] = (name,str(round(value, 2))+"%")
    return vMax

def stocksByDateByName(lst):
    dic = {}
    for i in lst:
        name = i[NAME]
        date = i[DATE]
        if date not in dic:
            dic[date] = {}
        dic[date][name] = {"OPEN":i[OPEN],"MAX":i[MAX],"MIN":i[MIN],"CLOSE":i[CLOSE],"VOLUME":i[VOLUME]}

    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for name in portfolio:
        val += stocks[date][name]["VOLUME"]*portfolio[name]/100
    return val

if __name__ == "__main__":
    main()
