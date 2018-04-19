# -*- coding:utf-8 -*-
"""
merge data file
"""

import pandas as pd

df_ad = pd.read_csv('../input/adFeature.csv', encoding='utf-8')
df_user = pd.read_csv('../input/userFeature.csv', encoding='utf-8')
# df_train = pd.read_csv('../input/train.csv', encoding='utf-8')

# df_train = pd.merge(left=df_train, right=df_ad, on='aid')
# df_train = pd.merge(left=df_train, right=df_user, on='uid')

# df_train.to_csv('../input/train_merge.csv', index=False, encoding='utf-8')
df_test = pd.read_csv('../input/test1.csv',encoding='utf-8')

df_test = pd.merge(left=df_test, right=df_ad, on='aid',how='inner')
df_test = pd.merge(left=df_test, right=df_user, on='uid')

df_test.to_csv('../input/test_merge.csv', index=False, encoding='utf-8')