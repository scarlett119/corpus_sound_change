# # This is the first script to process raw data, segmentation data obtained by forced alignment. 
# It outputs a data set file (.csv)


# # Read all csv files in a directory
# import os
# path = r'C:/Users/ziqi.chen/CYL/'
# files = os.listdir(path)
# for file in files:
# 	if '.csv' in file:
# 		full_file_path = os.path.join(path, file)
# 		print(full_file_path)
# 		with open(full_file_path ,'r', encoding='utf-8') as f:
# 			lines = f.readlines()


# # Or read a single csv file 
with open('C:/Users/ziqi.chen/1984-palign.csv','r',encoding="utf-8") as f:
	lines = f.readlines()
  
# # Set output file with header
write_file = open('C:/Users/ziqi.chen/1984_set.csv','w+',encoding="utf-8")
header = 'tag,start,end,token'+'\n'
write_file.write(header)

# # Creat a place-holder
hold_all = []

# Start from the second line (skip the header)
for line in lines[1:]:
	line = line.strip()
	line_split = line.split(',')
  
	# to change the start time and end time in the line list from strings to floats
	line_split[1] = float(line_split[1])
	line_split[2] = float(line_split[2])
  
	# line_split is already a list for each token, containing items separated by comma
	# here we put all line_splits in a list
	hold_all.append(line_split)

for i in hold_all:
	# # compare token lines and phoneme lines
	# to target at each token line
	if i[0] == 'TokensAlign':
  
		# then loop through hold_all again to find time-matched phoneme lines
		for e in hold_all:
			if e[0] == 'PhonAlign':
      
				# if the phoneme has the same starting time as the token,
				if e[1] == i[1]:
					# then it is a part of the token and we append the phoneme-token to the token line
					# here we only need the phoneme symbols
					i.append(e[3])
          
				# if the phoneme' the same starting time is later than that of the token,
				elif e[1] > i[1]:
					# meanwhile it is not later than the ending time of the the token
					if e[1] < i[2]:
						# then it is also a part of the token and we append it
						i.append(e[3])

		# Change numbers in the list to strings, to join them together
		i = ','.join([str(each) for each in i])+'\n'
    
    # output on this layer to get each token of its fule phoneme set, a.k.a. write file when the second loop ends
		write_file.write(i)
    
write_file.close()


