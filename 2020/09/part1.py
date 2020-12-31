preamble = []
preamblelen=25

def allsums(l):
    return set([ a + b for a in l for b in l if a != b])

def isvalid(l, i):
    return l[i] in allsums(l[i-preamblelen:i])


with open("input.txt", mode="r") as f:
    numbers = [ int(i.strip()) for i in f.readlines() ]

for i in range(preamblelen, len(numbers)):
    if not isvalid(numbers, i):
        print(numbers[i])
        exit(0)
