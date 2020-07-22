import pandas as pd

df = pd.DataFrame({'A': ['high', 'medium', 'low'],
                   'B': [10,20,30]},
                    index=[0, 1, 2])
print(df)

#######################################################
# Output
#######################################################
#        A   B
# 0    high  10
# 1  medium  20
# 2     low  30
#######################################################


#######################################################
# Creating Dummy Variables
#######################################################

# using get_dummies function of pandas package
df_with_dummies = pd.get_dummies(df, prefix='A', columns=['A'])
print (df_with_dummies)

#######################################################
# Output
#######################################################
#     B  A_high  A_low  A_medium
# 0  10       1      0         0
# 1  20       0      0         1
# 2  30       0      1         0
#######################################################


#######################################################
# Converting the Categorical Variable to Numerics
#######################################################

# using pandas package's factorize function
df['A_pd_factorized'] = pd.factorize(df['A'])[0]

# Alternatively you can use sklearn package's LabelEncoder function
from sklearn.preprocessing import LabelEncoder


le = LabelEncoder()
df['A_LabelEncoded'] = le.fit_transform(df.A)

print (df)
