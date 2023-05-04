def countDigits(str):
    count=0
    for i in str:
        if i.isdigit() == True:
            count += 1
    return count