import pandas as pd

df = pd.read_csv("../data/groupby.csv")
df.info()
print(df.head(n=3))
# ascending=True,默认是升序
sort_data = df.sort_values(by="Count",ascending=False)
print(sort_data)
print('分组的实现，分组之后每个组的索引就是分组的列')
group_data = df.groupby(by="Brand")
print(group_data,type(group_data))

for index,value in group_data:
    print('每个组的索引', index)
    print('每个组的记录', value)

print('计算每种品牌有多少件衣服')
# count,统计非空的行pandas中的count是对记录的每个列都进行统计
# print(group_data.count())
# print(group_data.sum())
print('1:',group_data['Count'].sum())
# 推荐分组方式
print('2:',df['Count'].groupby(by=df["Brand"]).sum())