import sys

##Initial variables
sourcefile = open(sys.argv[1])
associations = {}
finallist = []
counter = 0

##Iterate through the file line by line
for line in sourcefile:

        ##Split line into sections
        line = line.split('\n')[0]
        lineinfo = line.split('\t')

        ##Use a hash table to create associations between a key protein and its relevant information
        if lineinfo[0] not in associations.keys():
                if len(associations) >= 2000:
                        break
                associations[lineinfo[0]] = [lineinfo[1], lineinfo[3], 0]

        elif lineinfo[3] > associations[lineinfo[0]][1]:
                associations[lineinfo[0]] = [lineinfo[1], lineinfo[3], associations[lineinfo[0]][2]]

        associations[lineinfo[0]][2] += 1

##Move hash table into sorted list
for key in associations:
        finallist.append([key, associations[key][0], associations[key][1], associations[key][2]])

finallist.sort(key=lambda x:x[3])

#Return Results
for line in finallist:
        print(line)
