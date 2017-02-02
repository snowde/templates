bloom = train_new.reset_index()
bloom.reindex(train_new["id"])
train_new = train_new.fillna(a_mean)
id_df = train_new[col].groupby('id').agg([np.mean, np.std, len]).reset_index()

for o in range(len(train_new)):
id_df = bloom[col].groupby('id')
a_mean = id_df.mean().reset_index()
train_new = train_new.fillna(a_mean)
sum(train_new.isnull().sum(axis=1))

train["std"] = train.groupby('id').y.std()
corr = train.corr().ix["y", "std"]

merged = pd.merge(price, fiscal, on="date", how="outer")
