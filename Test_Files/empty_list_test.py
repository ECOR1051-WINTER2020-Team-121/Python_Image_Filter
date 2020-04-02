
FILE = open('test_file.txt', 'r')

for line in FILE:
    datalist = line.split()
    if len(datalist) < 3:
        datalist += [None]
    print(datalist)


FILE.close()
