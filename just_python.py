bloom = train_new.reset_index()
bloom.reindex(train_new["id"])
train_new = train_new.fillna(a_mean)
id_df = train_new[col].groupby('id').agg([np.mean, np.std, len]).reset_index()
