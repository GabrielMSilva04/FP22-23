from bisect import bisect_left

def convert_file_to_list(fname):
    with open(fname) as text:
        lst = [line[:-1] for line in text] #[:-1] to remove /n
    return lst

def bisectsearch(fname , string):
    lst = convert_file_to_list(fname)
    ind1 = bisect_left(lst , string)
    ind2 = bisect_left(lst , string[:-1] + chr(ord(string[-1])+1))
    words = lst[ind1:ind2]
    #return [words[i][len(string)] for i in range(len(words)) if len(words[i])>len(string) and (i==0 or words[i-1] != words[i])]
    return [w[len(string)] for w in words if len(w)>len(string)]

print(bisectsearch("Aula09/wordlist.txt" , "wiz"))