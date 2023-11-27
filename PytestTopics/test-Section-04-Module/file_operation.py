try:
    f = open("mfile.txt", 'r')
    #print(f.read())
    line = f.readline()
    #print(f.readlines())
    while line:
        print(line)
        line = f.readline()

finally:
    f.close()

with open("mfile.txt", "r") as f:
    print(f.readline())
    list2 = f.read().split('\n')
    print(list2)
