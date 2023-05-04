def allMatches(teams):
    assert len(teams) >= 2
    matches=[]
    for t1 in teams:
        for t2 in teams:
            if t1 != t2:
                m=(t1,t2)
                matches.append(m)
    return matches

def listTeams(teams):
    """Print the contents of the dictionary as a table, one item per row."""
    for team in teams:
        print("{}".format(team))

def addTeam(teams):
    team = str(input("Nome da equipa? "))
    if team not in teams:
        teams.append(team)
        print("Equipa Adicionada")
    else:
        print("Equipa já registada!")
    return teams
    
def registerResults(matches):
    results = {}
    for match in matches:
        print("Partida "+match[0]+":"+match[1])
        g1 = int(input("Golos marcados por "+match[0]+": "))
        g2 = int(input("Golos marcados por "+match[1]+": "))
        print()
        results[match] = (g1,g2)
    return results

def tabelapontos(matchesdic): #incompleto
    tabela = {}
    for match in matchesdic:
        if match[0] not in tabela:
            if matchesdic[match][0] > matchesdic[match][1]:
                tabela[match[0]] = 1
        if match[0] not in tabela:
            if matchesdic[match][0] > matchesdic[match][1]:
                tabela[match[1]] = 1
            


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar equipas")
    print("Listar (P)artidas")
    print("(A)dicionar equipa")
    #print("Procurar (N)úmero")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    teams = ["Benfica","Braga","Porto","Rocas"]

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("\nEquipas:")
            listTeams(teams)
        elif op == "A":
            print("\nAdicionar equipa:")
            addTeam(teams)
        elif op == "P":
            print("\nRegistar partidas:")
            resultados = registerResults(allMatches(teams))
            tabela = tabelapontos(resultados)
        else:
            print("Não implementado!")

main()