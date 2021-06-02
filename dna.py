import sys
import csv
import collections


y = []
de = collections.deque([])

def main():

    if len(sys.argv) != 3:
        print('Usage: python dna.py data.csv sequence.txt')
        sys.exit(1)

    # Opening and loading csv database
    data = []
    str_list = []
    temp = {}
    with open(sys.argv[1], 'r') as database:
        reader = csv.DictReader(database, delimiter = ',')
        for row in reader:
            keys = row.keys()
            str_list.append(row.keys())
            for i in keys:
                temp[i] = row[i]
            data.append(temp)

    str_list = list(str_list[0])[1:]

    # Read file from sequence txt
    dna = ''
    sequences = open(sys.argv[2], 'r')
    for i in sequences:
        dna += str(i)

    dna_list = []
    for i in dna:
        dna_list.append(i)

    sequences.close()

    #Initiating str match dictionary
    str_dict = {}
    for key in str_list:
        str_dict[key] = 0

    # Checking for str matches
    for STR in str_list:
        de.clear()
        y.clear()
        check(dna_list, STR)
        str_dict[STR] = max(y)

    print(str_dict)

def check(dna_list, STR):

    str_list = []
    for a in STR:
        str_list.append(a)
    i = -1
    match_count = 1

    #Loop through until detect turns true
    while detect(dna_list[i], STR) == False:
        i += 1
        if i == len(dna_list) - 1:
            break

    #When match is detected
    dna_list = dna_list[i + 1 : ]
    for index in range(0, len(dna_list) - 1, len(STR)):
        next_str = dna_list[index : (index + len(STR))]
        if next_str == str_list:
            match_count += 1
        else:
            y.append(match_count)
            dna_list = dna_list[index : ]
            break

    if len(dna_list) > 0:
        check(dna_list, STR)

def detect(char, STR):

    if len(de) >= len(STR):
        de.popleft()
        de.append(char)
    else:
        de.append(char)

    if ''.join(list(de)) == STR:
        detected = True
    else:
        detected = False

    return detected


main()

