# # this script is the second step, transforming side-by-side to stacked data
# each observation is represented by 8 lines for 8 F0 measurement points

# input file path
with open('C:/Users/ziqi.chen/PycharmProjects/CYLeung/1984.csv','r') as f:
	lines = f.readlines()

# path of output file with header
write_file = open('C:/Users/ziqi.chen/PycharmProjects/CYLeung/1984_stacked.csv','w+',encoding="utf-8")
header = 'word_type","year","duration","V_SPPAS","C2_SPPAS","vowel","F","Position","Faverage","single_tone","next_tone","ID_bug_add","'+'\n'
write_file.write(header)

# Start  from the second line: skip the header
for line in lines[1:]:
	line_split = line.split(',')
  
  # the items remain the same for each line of an observation
	before_unchange = line_split[1:7]
  after_unchange = line_split[15:]
  
  # the F0 points to be re-arranged 
	F1F8 = line_split[7:15]
  
  # now re-arrange them together with their orders
	for position, F0 in enumerate(F1F8):
		position = str(position)
 
    # put everything in a list, join them as string and output them
		write_file.write(','.join(before_unchange+[F0]+[position]+after_unchange))
