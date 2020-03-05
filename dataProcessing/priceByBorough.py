import pandas

# get an average price by borough
df = pandas.read_csv('../static/AB_NYC_2019.csv')
df = df.groupby(['neighbourhood_group'])['price'].mean().to_frame('avgPrice').reset_index()
print(df.head)
df.to_csv('priceByBorough.csv', index=False)
