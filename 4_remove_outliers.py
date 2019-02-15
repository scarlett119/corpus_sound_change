# # the fourth script is for identifying and removing the outliers in F0 data, based on 1.5xIQR rule

import pandas as pd
output_path = 'C:/Users/ziqi.chen/dataset_filtered.csv'
input_path = 'C:/Users/ziqi.chen/dataset.csv'
df = pd.read_csv(input_path, sep=',', header='infer')


# # Block 1: calculate quartiles

# place-holders for the upper/lower boundary at each time point (10 points in total)
upper = []
lower = []

# then calculate the first and third quartiles
for time in range(1,11): # range(1,5) means [1,2,3,4]

    # subset the whole datadrame by selecting rows based on values in a column in pandas
    subset_time = pd.DataFrame(df.loc[final['time'] == time])
    q1 = subset_time['f0'].quantile(q=0.25)
    q3 = subset_time['f0'].quantile(q=0.75)
    upper.append(q3 + 1.5*(q3 - q1))
    lower.append(q1 - 1.5*(q3 - q1))

# # Block 2: remove outlier using 1.5xIQR rule

# convert the whole dataframe to a list
final_list = df.values.tolist()

# a list to contain the observation ID for outliers
filter = []
for row in final_list:
    which = row[-2] - 1
    if row[-1] > upper[which] or row[-1] < lower[which]:
        if row[-4] not in filter:
            filter.append(row[-4])
            
# a new list to contain the data without outliers
filtered = []
for row in final_list:
    if row[-4] not in filter:
        filtered.append(row)

# convert the list into pandas dataframe and output it as csv file
filtered_df = pd.DataFrame(filtered, columns=['order_in_txt','char','phoneme','start','end','ID','tone','time','f0'])
filtered_df.to_csv(output_path,sep=',', float_format='%.2f', index_label='index')
