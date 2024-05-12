import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table(r'data_table.csv')

df_notyear = df.filter(items=['Vote from','Point', 'Jury', 'Public'])
df_notvotefrom = df.filter(items=['Year','Vote to', 'Point', 'Jury', 'Public'])
df_places = df_notvotefrom.groupby(['Year', 'Vote to']).sum(numeric_only=True).sort_values(['Year', 'Point'], ascending=[True, False])
df_mostpoints = df_notvotefrom.groupby(['Year', 'Vote to']).sum(numeric_only=True).sort_values('Point', ascending=False)
print('Sorted list by year and points.', df_places)
print('The most points.', df_mostpoints)

df_hu_to = df[df['Vote from'] == 'Hungary'].groupby(['Vote to']).agg({'Point' : ['mean', 'sum', 'count']}).sort_values(('Point', 'mean'), ascending=False)
df_hu_from =  df[df['Vote to'] == 'Hungary'].groupby(['Vote from']).agg({'Point' : ['mean', 'sum', 'count']}).sort_values(('Point', 'mean'), ascending=False)
df_hu = pd.concat([df_hu_to, df_hu_from], join='outer', axis=1)
print('Points and countries statistics that include Hungary.', df_hu)

df_hu_to_sum = df[df['Vote from'] == 'Hungary'].groupby(['Vote to']).agg({'Point' :  'sum'}).sort_values('Point', ascending=False)
df_hu_from_sum =  df[df['Vote to'] == 'Hungary'].groupby(['Vote from']).agg({'Point' :'sum'}).sort_values('Point', ascending=False)
df_hu_sum = pd.concat([df_hu_to_sum, df_hu_from_sum], join='outer',names=['Sum to','Sum from'], axis=1)

x1 = df_hu_sum.index[0:24]
y1 = df_hu_sum.values[0:24]
x2 = df_hu_sum.index[25:48]
y2 = df_hu_sum.values[25:48]

fig, ax = plt.subplots(2, 1)

ax[0].plot(x1, y1, '.-')
ax[1].plot(x2, y2, '.-')
plt.sca(ax[1])
plt.xticks(rotation=45, fontsize=7)
plt.ylabel('Sum')
plt.sca(ax[0])
plt.xticks(rotation=45, fontsize=7)
plt.ylabel('Sum')
plt.title('Points from and to Hungary')
plt.tight_layout()
plt.show()
