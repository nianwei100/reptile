import bar_chart_race as bcr
import pandas as pd

data_file = 'DXYArea.csv'
df = pd.read_csv(data_file, usecols=['countryName', 'province_confirmedCount', 'updateTime'])

df = df.loc[df.updateTime.astype(str).str.startswith('2022')]

df = df.groupby(['countryName', 'updateTime']).sum()

df.reset_index(inplace=True)

df['updateTime'] = pd.to_datetime(df['updateTime'])

df['updateTime'] = df['updateTime'].apply(lambda x: x.strftime('%Y-%m-%d'))


df2 = df.groupby(['countryName', 'updateTime']).apply(
	lambda t: t[t.province_confirmedCount == t.province_confirmedCount.max()]
)
df2.drop_duplicates(inplace=True)
df2.reset_index(inplace=True, drop=True)

df3 = df2.set_index(['updateTime', 'countryName'])['province_confirmedCount'].unstack()
df3.columns.name = None

df3.reset_index(inplace=True)


df3.fillna(0, inplace=True)
df3.set_index('updateTime', inplace=True)


# 生成结果文件
bcr.bar_chart_race(df=df3, filename='covid19_10.mp4', n_bars=30, title='2022全世界TOP30疫情确诊数量国家动态排名')
