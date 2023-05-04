CTP=float(input("Componente Teórico-Prática?"))
CP=float(input("Componente Prática? "))

if CTP<6.5 or CP<6.5:
    NOTA="reprovado"
    print("Nota final: 66")
elif 0.30*CTP+0.70*CP<10:
    NOTA="reprovado"
    print("Nota final:",CTP+CP)
else:
    NOTA="aprovado"
    NOTAF=0.30*CTP+0.70*CP
    print("Nota final:",NOTAF)

if NOTA=="reprovado":
    ATPR=float(input("ATPR? "))
    APR=float(input("APR? "))
    NOTAF=NR = 0.30*ATPR + 0.70*APR
    print("Nota final:", NOTAF)