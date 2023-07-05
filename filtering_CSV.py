import pandas as pd
# Read in the CSV file
df = pd.read_csv('Price-Estimate-Engine/data/generated_data_set.csv')

# Create a copy of the dataframe
filtered_df = df.copy()
indices_to_drop = []
indices_to_drop_2 = []

negatives = 0
strings = 0
for i in range(1,len(filtered_df)):
    try:
        value = float(df.loc[i,'price'])
    except:
        indices_to_drop_2.append(i)
        strings += 1
        continue
    if isinstance(value, (int, float)):
        if (value) < 0:
            indices_to_drop.append(i)
            negatives += 1

print(len(indices_to_drop))
print(len(indices_to_drop_2))
filtered_df = filtered_df.drop(indices_to_drop)
filtered_df = filtered_df.drop(indices_to_drop_2)
before_nAN = (len(filtered_df))
filtered_df = filtered_df.dropna()

after_nAN = (len(filtered_df))

print("Number of negative values: ", negatives)
print("Number of strings: ", strings)
print("Number of nAN: ", before_nAN-after_nAN)

csv_file = filtered_df.to_csv('Price-Estimate-Engine/data/generated_data_set1.csv',index=False)