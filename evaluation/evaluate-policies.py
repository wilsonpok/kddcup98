import pandas as pd
import numpy as np
from pathlib import Path

# Inputs
valtargt_file = 'http://kdd.ics.uci.edu/databases/kddcup98/epsilon_mirror/valtargt.txt'
val_pred_file = str(Path.home()) + '/kddcup98/data/val_binary_preds.csv'



#####################
# Load data
#####################

valtargt = pd.read_csv(valtargt_file)

val_preds = pd.read_csv(val_pred_file, header=None)
val_preds.columns = ['pred_vw']

val_preds['pred_model'] = val_preds['pred_vw'] - 1

val_preds['pred_model'].sum()
# 2413


[x.shape for x in [valtargt, val_preds]]
# [(96367, 3), (96367, 1)]

valtargt['TARGET_B'].value_counts()
# 0    91494
# 1     4873

val_preds['pred_model'].value_counts()
# 0    93954
# 1     2413

val_preds['pred_model'].value_counts(normalize=True)
# 0    0.97496
# 1    0.02504



#####################
# Compare policies
#####################

comparison = pd.DataFrame({'actual' : valtargt['TARGET_B'],
  'model' : val_preds['pred_model']})

comparison['random'] = comparison['model'].sample(frac=1, random_state=666)


