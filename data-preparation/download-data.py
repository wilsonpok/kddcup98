# http://kdd.ics.uci.edu/databases/kddcup98/kddcup98.html

import pandas as pd
import numpy as np



################
# Load data
################

lrn = pd.read_csv('http://kdd.ics.uci.edu/databases/kddcup98/epsilon_mirror/cup98lrn.zip')
val = pd.read_csv('http://kdd.ics.uci.edu/databases/kddcup98/epsilon_mirror/cup98val.zip')

[x.shape for x in [lrn, val]]
# [(95412, 481), (96367, 479)]

round(np.mean(lrn['TARGET_B']), 4)
# 0.0508

lrn['TARGET_B'].value_counts()
# 0    90569
# 1     4843

lrn['TARGET_B'].value_counts(normalize=True)
# 0    0.949241
# 1    0.050759


# validation data has OSOURCE = INF, training data doesn't
lrn = lrn.drop(['OSROUCE'], axis=1)
val = val.drop(['OSROUCE'], axis=1)



################
# Output data
################

lrn_output = pd.concat([lrn['TARGET_B'],
  lrn.drop(['TARGET_B', 'TARGET_D'], axis=1)], axis=1)

val_output = val.drop(['CONTROLN'], axis=1)

[x.shape for x in [lrn_output, val_output]]
# [(95412, 479), (96367, 478)]

lrn_output.to_csv('~/kddcup98/data/lrn_binary.csv', index=False)
val_output.to_csv('~/kddcup98/data/val_binary.csv', index=False)
