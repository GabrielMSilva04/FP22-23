from bisect import bisect_left

def convert_file_to_list(fname):
    with open(fname) as text:
        lst = [line[:-1] for line in text] #[:-1] to remove /n
    return lst

def bisectsearch(fname , string):
    lst = convert_file_to_list(fname)
    ind1 = bisect_left(lst , string)
    ind2 = bisect_left(lst , string[:-1] + chr(ord(string[-1])+1))
    n = ind2 - ind1
    return n

print(bisectsearch("wordlist.txt" , "wiz"))