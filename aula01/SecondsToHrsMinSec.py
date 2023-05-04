seconds=int(input("seconds?" ))

h=seconds//3600
hr=seconds%3600

m=hr//60
mr=hr%60

s=mr%60

print("{:02}:{:02}:{:02}".format(h, m, s))