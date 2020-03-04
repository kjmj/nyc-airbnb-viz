import pandas

# get an average price by neighborhood
df = pandas.read_csv('../static/AB_NYC_2019.csv')
df = df.groupby(['neighbourhood'])['price'].mean().to_frame('avgPrice').reset_index()
print(df.head)
df.to_csv('priceByNeighbourhood.csv', index=False)
