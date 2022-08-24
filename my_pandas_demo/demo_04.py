import pandas as pd

df = pd.read_csv("../data/groupby.csv")

sort_data = df.sort_values(by="Count", ascending=False)
print(sort_data)

group_data = df.groupby(by="Brand")
print(group_data, type(group_data))

for index, value in group_data :
    print("每个组的索引", index)
    print("每组的值", value)

print('每组有多少')
# print(group_data.count())
print(group_data.sum())

print(group_data['Count'].sum())

print(df['Count'].groupby(df["Brand"]).sum())
