# the third script is for switching from one phonetic symbol system to another
# originally, the data set includes phonetic annotations but the symbol set used is unwanted
# so we switch them to another set based on the mappings between two sets

# set the path of the output file
write_file = open(r'C:\Users\ziqi.chen\PycharmProjects\CYLeung\ouput.txt', 'w', encoding='utf-8')

# # create a dictionary to store the mappings between two sets of phonetic symbols
# key is for indexing; then replace key with value
d = {}

# Block 1: work on the mappings of the two sets of phonetic symbols first
with open(r'C:\Users\ziqi.chen\PycharmProjects\CYLeung\symbol_table.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()
    
    # each symbol to be replaced as a index (set A); the according symbol to replace it as the value of the index
    for line in lines:
        # the format of the mapping table: x = y
        # x: old symbols to be replaced
        # y: new symbols to replace
        d[line.split('=')[0].strip()] = line.split('=')[1].strip()

# Block 2: then move on to change phonetic symbols based on the mappings
with open(r'C:\Users\ziqi.chen\PycharmProjects\CYLeung\1984_set.csv', 'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_split = line.split(',')
        
        # to only work on the phonetic items of each line by defining the range of position
        # here it means start from the fifth item in a line and after
        for i in range(4, len(line_split)):
            # i is an index and d[i] is its value
            # here the values are the new symbol set, which replace the old ones
            line_split[i] = d[line_split[i]]
            
        write_file.write(','.join)
